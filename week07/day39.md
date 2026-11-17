# Day 39 - Agent（智能体）与 Tool Calling（工具调用）

## 核心知识点

### 1. 什么是 Agent（智能体）？
前几天的 RAG 只能“动嘴”（检索资料并回答），无法操作外部系统。
**Agent = 大模型（大脑）+ Tools（手脚）+ Executor（调度器）**。
它能够根据用户的意图，自主决定：需不需要调用工具？调用哪个？传什么参数？

### 2. Tool Calling（工具调用）原理
- **定义工具**：用 `@tool` 装饰器包裹普通的 Python 函数，函数的注释（docstring）就是给大模型看的“说明书”。
- **大模型不执行代码**：大模型只负责输出“我要调用 `calculate`，参数是 `expression='15-10'`”。真正执行函数的是 `AgentExecutor`。
- **闭环流程**：大模型输出指令 -> 执行器运行代码 -> 把运行结果返回给大模型 -> 大模型总结成人类语言。

### 3. ReAct 模式（Reasoning + Acting）
Agent 的核心运作逻辑，即“推理与行动交织”。
- 遇到问题先思考（Thought），判断是否需要工具。
- 如果需要，采取行动（Action）调用工具。
- 拿到观察结果（Observation），继续思考，直到能给出最终答案（Final Answer）。

## 产出
- `week07/day39_agent_basic.py`（包含天气查询工具与计算器工具的 Agent）

## 实战测试复盘（内心戏拆解）

### 测试 1：不需要工具（闲聊）
- 问：“你是谁？”
- 表现：Agent 判断无需调用工具，直接使用大模型自身的闲聊能力回答。

### 测试 2：多工具连续调用（逻辑规划）
- 问：“查北京天气，低于15度算15减10。”
- 表现：Agent 先调 `get_weather` 拿到北京气温，**自己在推理中判断满足条件**，接着调 `calculate` 算减法，最后把两次结果合并总结。完美展示多步推理。

### 测试 3：超出工具能力边界（防幻觉）
- 问：“查上海天气。”
- 表现：工具返回“暂不支持”，Agent 拿到报错后，诚实地向用户道歉，**没有瞎编天气**。

## 踩坑记录
- **LangChain 版本不兼容**：从 LangChain 1.0 开始，`AgentExecutor` 被废弃。
  报错：`ImportError: cannot import name 'AgentExecutor' from 'langchain.agents'`。
  解决：执行 `pip install langchain-classic`，并将导入路径改为 `from langchain_classic.agents import ...`。

## 明天（Day 40）
进入工作流编排神器 **LangGraph**，解决复杂多步任务下 Agent 容易陷入死循环的问题。
