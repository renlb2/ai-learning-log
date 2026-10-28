from transformers import pipeline

# 加载一个情感分析（Sentiment Analysis）流水线
# 默认会下载一个在英文文本上训练好的 BERT 小模型
print("正在加载模型...")
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# 测试两句话
texts = [
    "I love this movie, it's amazing and touching!",
    "This is the worst book I have ever read, totally a waste of time."
]

results = classifier(texts)

for text, res in zip(texts, results):
    print(f"\n文本: {text}")
    print(f"预测: {res['label']} (置信度: {res['score']:.4f})")
