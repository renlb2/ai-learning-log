# Day 19 - logging 替代 print

## 核心知识点
- logging 五级别 DEBUG/INFO/WARNING/ERROR/CRITICAL
- 双输出用 StreamHandler + FileHandler
- format 用 %(asctime)s [%(levelname)s] %(message)s
- logger.info("x=%s", var) 用占位符，不用 f-string
- logger.exception() 自动记录 traceback

## 产出
- week04/day19_organize.py
- week04/organize.log（运行日志，已 gitignore）

## 验证结果
- dry-run / execute 双模式正常
- 重名自动改名 a_1.py，WARNING 记录
- 不存在目录 ERROR 记录
- 日志追加模式，多次运行不覆盖

## 踩坑
- IndentationError: Tab 和空格混用，用 expand -t 4 统一
- 时间戳 %S 写成了 %-S，秒前少了冒号
- [MOVE] 日志 %s%s 少了斜杠，输出 markdownc.md

## 明天（Day 20）
综合项目：批量文件整理器 v1
