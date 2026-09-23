# Day 17 - shutil 移动文件 + 安全整理

## 核心知识点
- shutil.move 移动文件，shutil.copy2 复制并保留元数据
- Path.with_name() 换文件名，目录不变
- dry-run 模式：先打印计划，再执行
- safe_dest() 防覆盖，同名文件自动加 _1 _2
- RULES 字典做扩展名到目录的映射
- dest_dir.mkdir(exist_ok=True) 建目录不报错

## 产出
- week04/day17_organize.py
- 6 个测试文件正确归入 python / markdown / json / others

## 踩坑
- RULES 里 ".md" 写成了 "md"，导致所有 markdown 文件被扔进 others/
  原因：p.suffix 拿到的值一定带点，匹配时必须写 ".md"

## 明天（Day 18）
argparse：让脚本接收命令行参数
python day17_organize.py --target ./xxx --dry-run
