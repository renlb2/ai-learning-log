from transformers import pipeline

# 加载中文模型
classifier = pipeline("sentiment-analysis", model="uer/roberta-base-finetuned-jd-binary-chinese")

# 1. 看看模型内部的真实标签定义
print("模型的标签映射:", classifier.model.config.id2label)

# 2. 测试纯正的“京东式”评论
texts = [
    "手机收到了，质量非常好，物流很快，好评！",
    "衣服质量太差了，穿了一次就起球，必须退货！",
    "这部电影太好看了，强烈推荐！"
]

results = classifier(texts)
for t, r in zip(texts, results):
    print(f"文本: {t}")
    print(f"预测: {r['label']} (置信度: {r['score']:.4f})\n")
