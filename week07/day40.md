# Day 40 - LangGraph：用画流程图的方式控制大模型

## 核心知识点

### 1. 为什么需要 LangGraph？
传统的 `AgentExecutor` 像一个黑盒，大模型在里面怎么循环、何时停止，程序员很难干预。一旦遇到复杂的多步骤任务，容易陷入死循环或卡死。
**LangGraph** 将 Agent 的工作流变成了**状态机（StateGraph）**，像画流程图一样，把执行步骤固定下来，让 AI 的执行过程完全可控。

### 2. LangGraph 的三大核心要素
- **State（状态）**：一个贯穿全局的字典（TypedDict），所有节点共享和传递的数据袋子。
- **Node（节点）**：就是 Python 函数。接收 State 并返回修改后的 State。
- **Edge（边）**：定义节点之间的流转路线。
  - `add_edge`：固定连线（A 执行完必定去 B）。
  - `add_conditional_edges`：条件连线（根据函数的返回值，决定去 B 还是去 C）。

### 3. 工具调用循环（Agent 闭环）
如果只把大模型封装成一个节点，当模型决定调用工具时，它会输出 `tool_calls`，但不会真正执行代码，导致纯文本 `content` 为空。
在 LangGraph 中构建完整 Agent 需要三个关键节点/机制：
1. `chatbot` 节点：调用大模型，模型决定是否调用工具。
2. `ToolNode` 节点：专门负责执行大模型请求的工具代码。
3. `tools_condition` 路由：判断模型是否要调工具。如果要，走到 `ToolNode`；执行完后再走回 `chatbot` 节点形成循环，直到模型给出最终回答。

## 产出
- `week07/day40_langgraph_basic.py`（基础的文本处理流程图）
- `week07/day40_conditional.py`（带条件分支的语言判断流程）
- `week07/day40_langgraph_agent.py`（初版，暴露出没有工具执行节点的坑）
- `week07/day40_langgraph_full.py`（完整版，加入 `ToolNode` 和循环闭环）

## 踩坑记录
- **断头路导致输出为空**：在初版 `day40_langgraph_agent.py` 中，大模型识别出要算数，输出了 `tool_calls`，但图里没有工具执行节点。直接打印 `content` 导致无输出。
- **解法**：引入 `ToolNode(tools)` 和 `tools_condition`，增加 `tools -> chatbot` 的回环边，让工具执行结果能再次喂给大模型做总结。
- **版本问题回溯**：在 Day 39 遇到 `AgentExecutor` 无法导入，LangChain 1.0 之后需要安装 `langchain-classic` 或直接使用 LangGraph。

## 明天（Day 41）
RAG 的终极审判：RAGAS 自动化评测框架。
