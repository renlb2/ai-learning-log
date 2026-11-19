import os
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

load_dotenv()

# 1. 状态中包含消息列表（add_messages 是 LangGraph 特有的，能自动追加消息）
class State(TypedDict):
    messages: Annotated[list, add_messages]

# 2. 初始化大模型和工具
llm = ChatOpenAI(api_key=os.getenv("ZHIPU_API_KEY"), base_url="https://open.bigmodel.cn/api/paas/v4/", model="glm-4-flash")
@tool
def calculate(expression: str) -> str:
    """用于数学计算。"""
    return str(eval(expression))

tools = [calculate]
llm_with_tools = llm.bind_tools(tools)

# 3. 定义节点
def chatbot(state: State):
    # 模型接收当前状态里的消息，并可能决定调用工具
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# 构建图
builder = StateGraph(State)
builder.add_node("chatbot", chatbot)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)
graph = builder.compile()

# 运行
question = "帮我算一下 23 乘以 19 是多少？"
# 注意：这里必须使用 HumanMessage 对象
from langchain_core.messages import HumanMessage
result = graph.invoke({"messages": [HumanMessage(content=question)]})

# 打印最后一条消息
print("最终回答：", result["messages"][-1].content)
