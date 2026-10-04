# Day 20 - 综合项目：文件整理器 v1

## 项目产出
- projects/file-organizer/organizer.py
- projects/file-organizer/rules.json
- projects/file-organizer/README.md

## 综合运用的知识点
- pathlib：路径对象化
- shutil.move：文件移动
- argparse：命令行参数 + 互斥组
- logging：StreamHandler + FileHandler 双输出
- json：外部配置规则
- Counter：分类统计 + most_common
- time.time()：耗时统计

## 与 Day 19 的差异
- 规则外置 rules.json，改配置不改代码
- 新增 --verbose / --rules / --log 参数
- 结束时打印每类数量 + 耗时
- 独立项目目录 + README

## 验证结果
- 11 个测试文件正确分类
- 重名自动加 _1 后缀
- 不存在目录、非法 JSON、非目录路径均有 ERROR
- 日志双输出，追加模式

## 踩坑
- rules.json 多处语法错误：逗号在引号里、行尾少逗号、首行多 "json"
- 教训：JSON 写完立刻跑 `python -m json.tool 文件名.json`
- logger.warning 拼成了 waring，Python 报错信息直接给了正确拼写

## 下周（Week 05）
numpy + pandas + matplotlib，进入数据分析
