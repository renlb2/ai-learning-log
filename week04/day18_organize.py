from pathlib import Path
import shutil
import argparse
import sys

RULES = {
	".py": "python",
	".md": "markdown",
	".json": "json",
}

def safe_dest(dst: Path) ->Path:
	if not dst.exists():
		return dst
	stem, suffix = dst.stem,dst.suffix
	i = 1
	while True:
		new = dst.with_name(f"{stem}_{i}{suffix}")
		if not new.exists():
			return new
		i +=1

def parse_args():
	parser = argparse.ArgumentParser(description="按扩展名整理文件")
	parser.add_argument("--target",required=True,help="要整理的目录")
	group = parser.add_mutually_exclusive_group()
	group.add_argument("--dry-run",action="store_true",help="只打印计划，不移动（默认）")
	group.add_argument("--execute",action="store_true",help="真正执行移动")
	return parser.parse_args()

def organize(target:Path,dry_run:bool):
	if not target.exists():
		print(f"目录不存在：{target}")
		sys.exit(1)

	moved = 0
	for p in target.iterdir():
		if not p.is_file():
			continue
		ext = p.suffix.lower()
		sub = RULES.get(ext,"others")
		dest_dir = target/sub
		dest = safe_dest(dest_dir/p.name)
		if dry_run:
			print(f"[DRY-RUN]{p.name} -> {sub}/{dest.name}")
		else:
			dest_dir.mkdir(exist_ok=True)
			shutil.move(str(p),str(dest))
			print(f"[move]{p.name} -> {sub}/{dest.name}")
			moved +=1

	if dry_run:
		print("\n以上为预演，未移动文件。加--execute真正执行。")
	else:
		print(f"\n完成，共移动{moved}个文件。")
def main():
	args = parse_args()
	target = Path(args.target).expanduser().resolve()
	dry_run = not args.execute
	organize(target,dry_run)

if __name__ == "__main__":

	main()
