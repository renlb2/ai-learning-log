import jieba
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

docs = [
    "报销规定：打车费每月限额 500 元，凭发票报销。超过 500 元需部门总监审批。",
    "差旅住宿标准：一线城市 600 元/晚，二线城市 400 元/晚。",
    "考勤规定：上班时间是早上 9:00，迟到超过 3 次将扣除当月全勤奖。"
]
query = "500元怎么报销？"

# --- 获得向量排名 ---
model = SentenceTransformer("BAAI/bge-small-zh-v1.5")
vector_scores = cosine_similarity(model.encode([query]), model.encode(docs))[0]
# argsort 从大到小排，得到排名列表
vector_rank = vector_scores.argsort()[::-1] 

# --- 获得 BM25 排名 ---
bm25 = BM25Okapi([list(jieba.cut(d)) for d in docs])
bm25_scores = bm25.get_scores(list(jieba.cut(query)))
bm25_rank = bm25_scores.argsort()[::-1]

# --- RRF 融合 ---
def reciprocal_rank_fusion(rankings, k=60):
    rrf_scores = defaultdict(float)
    for rank_list in rankings:
        for position, doc_idx in enumerate(rank_list):
            # 核心公式：得分 = 1 / (k + 排名位置)
            # k 是一般设为 60 的平滑常数，防止第一名分数过于悬殊
            rrf_scores[doc_idx] += 1.0 / (k + position + 1)
    # 按得分降序排序
    return sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)

# 把两路排名传进去
final_ranking = reciprocal_rank_fusion([vector_rank, bm25_rank])

print("\n=== 混合检索（RRF 融合）最终结果 ===")
for idx, score in final_ranking:
    print(f"得分 {score:.4f} | {docs[idx]}")
