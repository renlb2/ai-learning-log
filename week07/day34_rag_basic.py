import os
import chromadb
from dotenv import load_dotenv
from openai import OpenAI
from chromadb.utils import embedding_functions

load_dotenv()

# ================= 1. 准备私有知识库 =================
# 假设这是你们公司的员工手册
documents = [
    "公司规定：员工每年享有 15 天的带薪年假，需提前 3 天在 OA 系统申请。",
    "报销规定：打车费每月限额 500 元，凭发票报销。超过 500 元需部门总监审批。",
    "考勤规定：上班时间是早上 9:00，迟到超过 3 次将扣除当月全勤奖。"
]

# 使用 HuggingFace 的本地轻量级向量模型（把文字转成数字坐标）
hf_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# 初始化本地内存向量数据库
client = chromadb.Client()
collection = client.create_collection(name="company_rules", embedding_function=hf_ef)

# 把文档塞进数据库，并自动生成向量
collection.add(
    documents=documents,
    ids=["doc1", "doc2", "doc3"]
)
print("知识库已加载完毕！")

# ================= 2. 检索（Retrieval） =================
user_question = "我今天 9 点半到公司，会扣钱吗？"
print(f"\n用户提问: {user_question}")

# 在数据库里搜索最相关的 1 条文档
results = collection.query(
    query_texts=[user_question],
    n_results=1
)

# 提取检索到的背景知识
retrieved_context = results['documents'][0][0]
print(f"\n[检索到的参考资料]: {retrieved_context}")

# ================= 3. 生成（Generation） =================
# 初始化智谱大模型
llm = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)

# 构造 Prompt：强制要求大模型只能根据资料回答
prompt = f"""
你是一个企业智能客服。请严格根据下面提供的【参考资料】回答用户的【问题】。
如果参考资料中没有相关信息，请直接回答“不知道”，绝对不要自己编造。

【参考资料】：
{retrieved_context}

【问题】：
{user_question}
"""

response = llm.chat.completions.create(
    model="glm-4-flash",
    temperature=0,
    messages=[{"role": "user", "content": prompt}]
)

print(f"\n[AI 最终回答]:\n{response.choices[0].message.content}")
