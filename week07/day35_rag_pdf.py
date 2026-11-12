import os
import chromadb
from dotenv import load_dotenv
from openai import OpenAI
from chromadb.utils import embedding_functions
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader  # 如果你有PDF文件的话

load_dotenv()

# ================= 1. 读取长文档 =================
# 【模拟读取 PDF】如果你有 pdf，取消下面 3 行的注释，并改成你的文件名
# reader = PdfReader("test.pdf")
# long_text = "".join([page.extract_text() for page in reader.pages])

# 【备用：模拟长文本】
long_text = "公司规定：员工每年享有 15 天的带薪年假，需提前 3 天在 OA 系统申请。报销规定：打车费每月限额 500 元，凭发票报销。超过 500 元需部门总监审批。考勤规定：上班时间是早上 9:00，迟到超过 3 次将扣除当月全勤奖。食堂规定：中午 12:00 开饭，员工免费就餐，禁止打包。"

# ================= 2. 切片 =================
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)
chunks = text_splitter.split_text(long_text)
print(f"文档被切成了 {len(chunks)} 块。")

# ================= 3. 存入向量库 =================
hf_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="BAAI/bge-small-zh-v1.5")
client = chromadb.Client()
collection = client.create_collection(name="company_docs", embedding_function=hf_ef)

# 把每一块存进去，并给它们编个号
collection.add(
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)

# ================= 4. 检索并生成 =================
user_question = "打车费超过500元怎么办？"
print(f"\n用户提问: {user_question}")

# 找最相关的 2 块（因为答案可能分散在相邻的两块里）
results = collection.query(query_texts=[user_question], n_results=2)
retrieved_context = "\n---\n".join(results['documents'][0])

print(f"\n[检索到的参考资料]:\n{retrieved_context}")

llm = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)

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
