from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
classifier_cn = pipeline("sentiment-analysis", model="uer/roberta-base-finetuned-jd-binary-chinese")

my_text = "The weather is so beautiful today, I feel great!" # 换成你想说的
my_text_cn = "这部电影太好看了，强烈推荐！"
result = classifier(my_text)
result_cn = classifier(my_text_cn)
print(result)
print(result_cn)
