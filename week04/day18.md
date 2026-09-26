# Day 18 - argparse 命令行工具

## 核心知识点
- ArgumentParser 解析命令行参数
- required=True 必填参数
- action="store_true" 开关型参数
- mutually_exclusive_group() 互斥参数
- Path(args.target).expanduser().resolve() 展开 ~ 并转绝对路径
- sys.exit(1) 异常退出
- 默认 dry-run 更安全

## 产出
- week04/day18_organize.py
- 6 项测试全部通过

## 踩坑
- dry-run 没输出 [DRY-RUN] 行，原因不是脚本 bug，而是 test_organize 顶层文件已被 Day 17 移进子目录，iterdir 找不到文件
- 测试前要先重置测试数据

## 明天（Day 19）
logging 模块：把 print 换成 logging，输出带时间戳的日志文件
