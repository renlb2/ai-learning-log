import os
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()

# 1. 定义状态
class State(TypedDict):
    messages: Annotated[list, add_messages]

# 2. 初始化大模型和工具
llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"), 
    base_url="https://open.bigmodel.cn/api/paas/v4/", 
    model="glm-4-flash"
)

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

# 节点 1：大模型思考
builder.add_node("chatbot", chatbot)

# 节点 2：LangGraph 自带的工具执行节点（帮你执行 calculate）
builder.add_node("tools", ToolNode(tools))

# 起点出发，先找大模型
builder.add_edge(START, "chatbot")

# 条件边：大模型回答后，判断是否需要调工具？
# tools_condition 是官方写好的路由：如果模型要调工具，去 "tools" 节点；否则去 END
builder.add_conditional_edges("chatbot", tools_condition)

# 工具执行完后，必须回到大模型（让它根据工具结果做最终总结）
builder.add_edge("tools", "chatbot")

graph = builder.compile()

# 4. 运行
from langchain_core.messages import HumanMessage
question = "帮我算一下 23 乘以 19 是多少？"
print(f"用户提问：{question}")

result = graph.invoke({"messages": [HumanMessage(content=question)]})

# 打印最后一条消息
print("\n最终回答：", result["messages"][-1].content)
