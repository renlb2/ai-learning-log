import seaborn as sns
sns.set_theme(style="whitegrid")    # 先调

import matplotlib
import matplotlib.font_manager as fm
FONT_PATH = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
fm.fontManager.addfont(FONT_PATH)
FONT_NAME = fm.FontProperties(fname=FONT_PATH).get_name()
matplotlib.rcParams["font.family"] = FONT_NAME
matplotlib.rcParams["axes.unicode_minus"] = False

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ===== 字体设置：先试 Noto Sans CJK SC，不行就换 =====
#matplotlib.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "WenQuanYi Micro Hei"]
#matplotlib.rcParams["axes.unicode_minus"] = False

#sns.set_theme(style="whitegrid")

# ===== 数据 =====
df = pd.DataFrame({
    "class":   ["A", "A", "A", "B", "B", "B", "B"],
    "name":    ["小明", "小红", "小刚", "小美", "小强", "小丽", "小华"],
    "gender":  ["M", "F", "M", "F", "M", "F", "M"],
    "math":    [85, 92, 82, 95, 60, 88, 72],
    "english": [88, 84.5, 80, 92, 72, 85, 90],
})

# ===== 图 1：柱状图 - 每个学生的数学成绩 =====
fig, ax = plt.subplots(figsize=(8, 5))
# TODO 1：用 ax.bar 画柱状图，x=name，height=math
# 提示：ax.bar(df["name"], df["math"], color="steelblue")
ax.bar(df["name"],df["math"],color="steelblue")
ax.set_title("每个学生的数学成绩")
ax.set_xlabel("学生")
ax.set_ylabel("数学分数")
ax.grid(True, alpha=0.3, axis="y")
fig.savefig("week05/plot_bar.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ===== 图 2：散点图 - 数学 vs 英语 =====
fig, ax = plt.subplots(figsize=(8, 5))
# TODO 2：用 ax.scatter 画散点，x=math，y=english
ax.scatter(df["math"],df["english"],alpha=0.6)
ax.set_title("数学 vs 英语成绩")
ax.set_xlabel("数学")
ax.set_ylabel("英语")
ax.grid(True, alpha=0.3)
fig.savefig("week05/plot_scatter.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ===== 图 3：直方图 - 数学分数分布 =====
fig, ax = plt.subplots(figsize=(8, 5))
# TODO 3：用 ax.hist 画直方图，bins=5
ax.hist(df["math"],bins=20,edgecolor="black")
ax.set_title("数学成绩分布")
ax.set_xlabel("分数")
ax.set_ylabel("人数")
fig.savefig("week05/plot_hist.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ===== 图 4：seaborn 箱线图 - 按班级看数学分布 =====
fig, ax = plt.subplots(figsize=(8, 5))
# TODO 4：用 sns.boxplot 画箱线图，x=class，y=math
sns.boxplot(data=df,x="class",y="math")
ax.set_title("各班级数学成绩分布")
fig.savefig("week05/plot_box.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ===== 图 5：seaborn 热力图 - 相关性 =====
fig, ax = plt.subplots(figsize=(6, 5))
# TODO 5：用 sns.heatmap 画热力图，数据是数值列的相关性
# 提示：df[["math", "english"]].corr()
sns.heatmap(df.corr(numeric_only=True),annot=True,cmap="coolwarm")
ax.set_title("成绩相关性")
fig.savefig("week05/plot_heatmap.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("已生成 5 张图片到 week05/")
