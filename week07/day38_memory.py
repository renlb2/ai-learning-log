import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    model="glm-4-flash",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个友好的助手。"),
    # 这里预留一个位置，专门放历史对话
    ("placeholder", "{chat_history}"),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()

# 模拟对话历史（手动维护一个列表）
chat_history = []

# 第一轮
q1 = "我叫王小明，是一名程序员。"
a1 = chain.invoke({"chat_history": chat_history, "question": q1})
print(f"用户: {q1}\nAI: {a1}\n")

# 把第一轮加入历史
chat_history.append(HumanMessage(content=q1))
chat_history.append(AIMessage(content=a1))

# 第二轮
q2 = "你还记得我叫什么名字吗？我的职业是什么？"
a2 = chain.invoke({"chat_history": chat_history, "question": q2})
print(f"用户: {q2}\nAI: {a2}")
