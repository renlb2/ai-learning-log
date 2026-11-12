# Day 34 - Self-Attention 机制
## 关键发现
- 大模型没有记忆，不能改内部参数，所以用 RAG（开卷考试）解决幻觉。
- Embedding（向量化）：把文字映射到高维空间的坐标点。意思相近的句子，坐标距离也相近。
- 向量数据库（ChromaDB）：专门用来存这些坐标，并做“距离计算”找相似内容。

## 产出
- day34_rag_basic.py 
- day34_rag_add.py
