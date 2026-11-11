import torch
import matplotlib
matplotlib.use('Agg')  # 解决无界面环境报错
import matplotlib.pyplot as plt
import seaborn as sns
from transformers import AutoTokenizer, AutoModel

# 设置中文字体
matplotlib.rcParams["font.sans-serif"] = ["Noto Sans CJK SC"]
matplotlib.rcParams["axes.unicode_minus"] = False

# 1. 加载模型（这里用 distilbert，轻量且快）
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
# 关键：output_attentions=True 告诉模型把注意力权重留下来
model = AutoModel.from_pretrained(model_name, output_attentions=True)

# 2. 准备输入文本（经典的指代消解句子）
text = "The animal didn't cross the street because it was too tired"

# 3. 把文本转成模型认识的数据
inputs = tokenizer(text, return_tensors="pt")
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

# 4. 模型推理
outputs = model(**inputs)
# outputs.attentions 是一个元组，包含每一层的注意力矩阵
# 形状: (batch_size, num_heads, sequence_length, sequence_length)
attentions = outputs.attentions

# 5. 提取并可视化
# 我们选择最后一层（第 6 层，索引为 5），第一个注意力头（Head 0）
layer = 5
head = 0
attention_matrix = attentions[layer][0, head].detach().numpy()

# 画图
plt.figure(figsize=(10, 8))
sns.heatmap(
    attention_matrix, 
    xticklabels=tokens, 
    yticklabels=tokens, 
    cmap="viridis"
)
plt.title(f"Attention Weights (Layer {layer+1}, Head {head+1})")
plt.xlabel("Key (被关注的词)")
plt.ylabel("Query (发起关注的词)")
plt.xticks(rotation=45, ha='right')

# 保存图片
plt.tight_layout()
plt.savefig("week07/attention_map.png", dpi=150)
print("图片已保存为 week07/attention_map.png")
