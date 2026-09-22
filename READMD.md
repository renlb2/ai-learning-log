# AI Learning Log

零基础转 AI 应用工程师（LLM / RAG / Agent 方向）的 26 周学习记录。

本仓库用于：
- 逐日记录学习内容、代码、踩坑
- 沉淀可复习的知识卡片与错题
- 展示端到端项目作品集

---

## 目标与路径

| 项目 | 内容 |
|---|---|
| 主目标 | 6 个月内拿到第一个 AI 应用 / LLM 工程岗面试机会 |
| 学习周期 | 2026-08-26 → 2027-02-21（26 周） |
| 每周投入 | 5 小时（工作日 40 分钟 + 周末 2.5 小时） |
| 技术主线 | Python → 机器学习 → LLM API → RAG → Agent |
| 明确放弃 | CV、强化学习、数学专项（工程岗按需补直觉） |

详见：`docs/plan.md`（Excel 计划表）

---

## 进度总览

### 阶段一：Python 地基（6 周）

#### Week 01 · Python 起步

| Day | 主题 | 产出 |
|---|---|---|
| Day 1 | 环境搭建：Python 3.12 + VS Code + Git | 仓库初始化 |
| Day 2 | 变量、数据类型、字符串格式化 | BMI 计算器 |
| Day 3 | 条件判断 if-elif-else、逻辑运算符 | 成绩等级小程序 |
| Day 4 | for/while、break/continue、嵌套循环 | 猜数字游戏 |
| Day 5 | 列表、元组、字典、集合 | 本周语法速查表 |

#### Week 02 · 函数与文件

| Day | 主题 | 产出 |
|---|---|---|
| Day 6 | 函数定义、参数、返回值 | BMI 脚本函数化重构 |
| Day 7 | 作用域、lambda、列表推导式 | 重构 3 段旧代码 |
| Day 8 | 字符串进阶：切片、split/join、re 入门 | 日志解析工具 |
| Day 9 | 文件读写 txt / csv | CSV 统计脚本 |
| Day 10 | 异常处理 try/except/finally | 旧脚本加错误处理 |
| Day 11 | 模块与包、pip、requests | API 数据抓取 |
| Day 12 | 综合项目：命令行待办清单 | **TodoManager**（增删改查 + JSON 持久化） |

#### Week 03 · 面向对象

| Day | 主题 | 产出 |
|---|---|---|
| Day 13 | 类、属性、方法、`__init__`、继承 | `Contact` 基类 + 2 个子类 |
| Day 14 | 参数校验、异常处理、unittest | **ContactManager** + 8 个单测 |
| Day 15 | pathlib 重构、自动备份 | 通讯录迁移到 `data/`，含备份逻辑 |

#### Week 04 · 标准库（进行中）

| Day | 主题 | 状态 |
|---|---|---|
| Day 16 | datetime + collections + 文件整理脚本 | 待开始 |
| Day 17 | os / shutil 进阶：移动、复制、重命名 | 待开始 |
| Day 18 | argparse / 命令行工具 | 待开始 |
| Day 19 | 日志 logging 模块 | 待开始 |
| Day 20 | 综合项目：批量文件整理器 | 待开始 |
| Day 21 | 周复盘 + 检查点自测 | 待开始 |

---

## 目录结构

```text
ai-learning-log/
├── README.md
├── week01/              # 基础语法（Day 1-5）
├── week02/              # 函数与文件（Day 6-12）
│   ├── todo_file.py
│   ├── address_book_json.py
│   └── exception_demo.py
├── week03/              # 面向对象（Day 13-15）
│   ├── contacts_class.py
│   └── data/
│       ├── contacts.json
│       └── backup/
│           └── contacts_backup.json
├── week04/              # 标准库（Day 16-21）
├── projects/            # 端到端项目（阶段二起）
├── notes/               # 速查表、知识卡片
│   └── errors.md        # 踩坑与错题记录
└── chat-log/            # 每周复盘总结
    └── week03-summary.md
