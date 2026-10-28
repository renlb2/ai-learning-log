from transformers import AutoTokenizer

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)

text = "I love this movie!"
tokens = tokenizer.tokenize(text)
print(f"原始文本: {text}")
print(f"切分后的 Token: {tokens}")

ids = tokenizer.encode(text)
print(f"Token 对应的 ID: {ids}")

decoded = tokenizer.decode(ids)
print(f"根据 ID 还原的文本: {decoded}")
