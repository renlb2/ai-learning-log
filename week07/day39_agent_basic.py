import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# 1. 初始化大模型
llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    model="glm-4-flash",
    temperature=0
)

# ================= 2. 定义工具（Tools） =================
# 使用 @tool 装饰器，大模型能自动读取函数的注释（docstring）来理解工具的作用

@tool
def calculate(expression: str) -> str:
    """用于数学计算。输入一个合法的 Python 数学表达式，比如 '123 * 456'。"""
    try:
        # 注意：真实生产环境中禁止直接使用 eval，这里仅作教学演示
        result = eval(expression)
        return f"计算结果为: {result}"
    except Exception as e:
        return f"计算失败: {e}"

@tool
def get_weather(city: str) -> str:
    """用于查询指定城市的天气。输入城市名称，如 '北京' 或 '洛阳'。"""
    # 模拟调用外部天气 API
    mock_data = {
        "洛阳": "晴天，气温 15-25度，微风。",
        "北京": "多云，气温 10-18度，北风3级。"
    }
    return mock_data.get(city, "抱歉，暂不支持该城市的天气查询。")

# 把工具放进列表
tools = [calculate, get_weather]

# ================= 3. 构建 Agent =================
# 定义 Agent 的系统提示词，要求它必须使用工具
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个强大的 AI 助手。你可以使用提供的工具来解决问题。"),
    ("human", "{input}"),
    # Agent 运行时的中间思考过程会自动存入 {agent_scratchpad}
    ("placeholder", "{agent_scratchpad}"),
])

# 创建支持工具调用的 Agent
agent = create_tool_calling_agent(llm, tools, prompt)
# AgentExecutor 负责循环执行：调用模型 -> 发现要调工具 -> 执行工具 -> 结果再给模型
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# ================= 4. 测试提问 =================
#print("========== 测试 1：数学计算 ==========")
#res1 = agent_executor.invoke({"input": "帮我算一下 1234 乘以 5678 等于多少？"})
#print(f"\n最终回答: {res1['output']}")

#print("\n========== 测试 2：查天气 ==========")
#res2 = agent_executor.invoke({"input": "洛阳今天天气怎么样？适合穿短袖吗？"})
#print(f"\n最终回答: {res2['output']}")


print("\n========== 测试 3：查不需要工具的问题=========")
res3 = agent_executor.invoke({"input": "你好，请问你是谁？"})
print(f"\n最终回答: {res3['output']}")

print("\n========== 测试 4：测试多工具连续调用：==========")
res4 = agent_executor.invoke({"input": "帮我查一下北京的天气，如果气温低于 15 度，帮我算一下 15 减 10 等于多少。"})
print(f"\n最终回答: {res4['output']}")

print("\n========== 测试 3：查超出工具能力的问题=========")
res5 = agent_executor.invoke({"input": "帮我查一下上海的天气。"})
print(f"\n最终回答: {res5['output']}")
