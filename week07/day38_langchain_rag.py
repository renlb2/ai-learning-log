import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

# 1. 初始化大模型（智谱兼容 OpenAI 格式）
llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    model="glm-4-flash",
    temperature=0
)

# 2. 准备数据并存入 Chroma
# 注意：LangChain 的文档对象叫 Document，带 page_content 属性
docs = [
    Document(page_content="公司规定：员工每年享有 15 天的带薪年假，需提前 3 天在 OA 系统申请。"),
    Document(page_content="报销规定：打车费每月限额 500 元，凭发票报销。超过 500 元需部门总监审批。"),
    Document(page_content="考勤规定：上班时间是早上 9:00，迟到超过 3 次将扣除当月全勤奖。")
]

# 使用本地 BGE 中文向量模型
# 注意：这里可能需要你之前已经下载过该模型
#embeddings = OpenAIEmbeddings(
#   api_key=os.getenv("ZHIPU_API_KEY"), # 智谱也有 embedding API，但这里为了不额外收费，我们用本地
#   base_url="https://open.bigmodel.cn/api/paas/v4/",
#   model="embedding-2" 
#) 
# （注：上面用的是智谱的 embedding API，如果你没开通，我们可以换回本地，这里我提供本地写法：）
from langchain_community.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5")

# 一键存入向量库（自动完成切片、向量化、入库）
vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 3. 定义 Prompt 模板
prompt = ChatPromptTemplate.from_template("""
你是一个严谨的客服。请完全基于以下 <资料> 回答。
如果资料里没写，直接回答“不知道”，绝对不许自己编造！

<资料>
{context}
</资料>

问题：{question}
""")

# 4. 组装 LCEL（LangChain 表达式语言）流水线
# 这是一个超级好用的语法，用 | 符号像水管一样把流程连起来
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 5. 发起提问
question = "我打车花了 600 块钱，能报销吗？"
print(f"用户提问: {question}\n")

# 一键运行
answer = rag_chain.invoke(question)
print(f"AI 回答:\n{answer}")
