import jieba
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 1. 模拟知识库
docs = [
    "报销规定：打车费每月限额 500 元，凭发票报销。超过 500 元需部门总监审批。",
    "差旅住宿标准：一线城市 600 元/晚，二线城市 400 元/晚。",
    "考勤规定：上班时间是早上 9:00，迟到超过 3 次将扣除当月全勤奖。"
]

query = "500元怎么报销？"

# ================= 检索器 A：向量检索 =================
print("正在加载向量模型...")
model = SentenceTransformer("BAAI/bge-small-zh-v1.5")
doc_embeddings = model.encode(docs)
query_embedding = model.encode([query])

# 算余弦相似度
similarities = cosine_similarity(query_embedding, doc_embeddings)[0]
# 排序并取最高的
vector_top_idx = similarities.argsort()[::-1][0]

print("\n=== 纯向量检索结果 ===")
print(f"匹配到: {docs[vector_top_idx]}")
# （注：如果你发现它匹配到了 600元住宿，说明向量模型对数字确实不敏感）

# ================= 检索器 B：BM25 关键词检索 =================
# 2. 先用 jieba 把句子切成词
tokenized_docs = [list(jieba.cut(doc)) for doc in docs]
# 3. 建 BM25 索引
bm25 = BM25Okapi(tokenized_docs)

tokenized_query = list(jieba.cut(query))
# 4. 计算 BM25 分数
bm25_scores = bm25.get_scores(tokenized_query)
# 排序并取最高的
bm25_top_idx = bm25_scores.argsort()[::-1][0]

print("\n=== 纯 BM25 检索结果 ===")
print(f"匹配到: {docs[bm25_top_idx]}")
