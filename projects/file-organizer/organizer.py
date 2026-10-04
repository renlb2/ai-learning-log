
#!/usr/bin/env python3
"""文件整理器v1-按扩展名分类整理文件"""

import argparse
import json
import logging
import shutil
import sys
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

#-------------日志------------
logger = logging.getLogger("organizer")
def setup_logger(verbose:bool,log_file:Path):
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    fmt = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG if verbose else logging.INFO)
    console.setFormatter(fmt)

    fh = logging.FileHandler(log_file,encoding = "utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)

    logger.addHandler(console)
    logger.addHandler(fh)

#----------配置加载----------
def load_rules(path:Path) -> dict:
    if not path.exists():
       logger.error("规则文件不存在：%s",path)
       sys.exit(1)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        logger.error("规则文件不是合法 JSON：%S",e)
        sys.exit(1)
    #反转：扩展名->目标目录名
    ext_to_dir = {}
    for dir_name,exts in data.items():
        for ext in exts:
            ext_to_dir[ext.lower()] = dir_name
    logger.info("已加载 %d 条扩展名规则",len(ext_to_dir))
    return ext_to_dir

#----------防覆盖----------
def safe_dest(dst:Path)->Path:
    if not dst.exists():
        return dst
    stem,suffix = dst.stem,dst.suffix
    i = 1
    while True:
        new = dst.with_name(f"{stem}_{i}{suffix}")
        if not new.exists():
            logger.warning("目标已存在，改名 %s",new.name)
            return new
        i += 1

#----------主流程----------
def organize(target:Path,rules:dict,dry_run:bool):
    if not target.exists():
        logger.error("目标目录不存在：%s",target)
        sys.exit(1)
    if not target.is_dir():
        logger.error("目标不是目录：%s",target)
        sys.exit()

    start = time.time()
    stats = Counter()
    moved = 0

    for p in sorted(target.iterdir()):
        if not p.is_file():
            continue

        ext = p.suffix.lower()
        sub = rules.get(ext,"others")
        dest_dir = target / sub
        dest = safe_dest(dest_dir / p.name)

        if dry_run:
            logger.info("[DRY_RUN] %s -> %s/%s",p.name,sub,dest.name)
            stats[sub] += 1
        else:
            dest_dir.mkdir(exist_ok=True)
            try:
                shutil.move(str(p),str(dest))
                logger.info("[MOVE] %s -> %s/%s",p.name,sub,dest.name)
                stats[sub] += 1
                moved += 1
            except Exception:
                logger.exception("移动失败：%s",p.name)

        elapsed = time.time() - start

    #汇总
    logger.info("=" *40)
    if dry_run:
        logger.info("预演完成，未移动文件")
    else:
        logger.info("完成，共移动 %d 个文件",moved)
    logger.info("耗时 %.2f 秒",elapsed)
    logger.info("分类统计：")
    for sub,cnt in stats.most_common():
        logger.info("  %-12s：%d",sub,cnt)

#----------命令行----------
def parse_args():
    parser = argparse.ArgumentParser(
        description="按扩展名整理目录中的文件",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="示例：\n"
            " python organize.py --target ~/Downloads --dry-run\n"
            " python orgznize.py --target ~/Downloads --execute\n"
    )
    parser.add_argument("--target",required=True,help="要整理的目录")
    parser.add_argument("--rules",default="rules.json",help="规则文件路径，默认rules.json")
    parser.add_argument("--log",default="organizer.log",help="日志文件路径，默认organizer.log")
    parser.add_argument("--verbose",action="store_true",help="显示 DEBUG 级别日志")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--dry-run",action="store_true",help="只打印，不移动（默认）")
    group.add_argument("--execute",action="store_true",help="真正执行移动")

    return parser.parse_args()

def main():
    args = parse_args()

    target = Path(args.target).expanduser().resolve()
    rules_path = Path(args.rules).expanduser().resolve()
    log_path = Path(args.log).expanduser().resolve()

    setup_logger(args.verbose,log_path)

    logger.info("=" * 40)
    logger.info("目标目录：%s",target)
    logger.info("规则文件：%s",rules_path)
    logger.info("模式：%s","执行" if args.execute else "预演")

    rules = load_rules(rules_path)
    organize(target,rules,dry_run=not args.execute)

if __name__ == "__main__":
    main()
