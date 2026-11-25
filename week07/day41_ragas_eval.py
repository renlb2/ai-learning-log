import os
from dotenv import load_dotenv
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from datasets import Dataset
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper

load_dotenv()

# 1. 初始化 RAGAS 需要的“裁判”（用智谱大模型和本地向量模型）
llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    model="glm-4-flash",
    temperature=0
)
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5")

# 包装成 RAGAS 认识的格式
ragas_llm = LangchainLLMWrapper(llm)
ragas_embeddings = LangchainEmbeddingsWrapper(embeddings)

# 2. 准备测试数据集
# 包含：问题(question)、AI的回答(answer)、检索到的上下文(contexts)、标准答案(ground_truth)
data = {
    "question": [
        "公司年假有几天？",
        "打车费超过500元怎么报销？",
        "公司食堂几点开饭？"
    ],
    "answer": [
        "员工每年享有15天带薪年假。",
        "需要凭发票，并经过部门总监、CEO、董事长三重签字审批。", 
        "中午12点开饭，而且是免费的。" 
    ],
    "contexts": [
        ["公司规定：员工每年享有 15 天的带薪年假，需提前 3 天在 OA 系统申请。"],
        ["报销规定：打车费每月限额 500 元，凭发票报销。超过 500 元需部门总监审批。"],
        ["食堂规定：中午 12:00 开饭，员工免费就餐，禁止打包。"]
    ],
    "ground_truth": [
        "15天。",
        "超过500元需部门总监审批。",
        "中午12点开饭，员工免费。" 
    ]
}

dataset = Dataset.from_dict(data)

# 3. 设置裁判的打分规则
metrics = [
    faithfulness, 
    answer_relevancy, 
    context_precision
]

# 4. 开始评测
print("开始评测，请稍候（大模型打分需要时间）...")
result = evaluate(
    dataset=dataset,
    metrics=metrics,
    llm=ragas_llm,
    embeddings=ragas_embeddings
)

# 5. 打印成绩单
print("\n========== 评测结果 ==========")
print(result)
