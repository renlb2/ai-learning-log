import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

#matplotlib.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "WenQuanYi Micro Hei"]
#matplotlib.rcParams["axes.unicode_minus"] = False
#sns.set_theme(style="whitegrid")

from matplotlib import font_manager

# 手动把 Noto CJK 字体注册给 matplotlib
for f in font_manager.findSystemFonts(fontpaths=["/usr/share/fonts/opentype/noto/"]):
    if "NotoSansCJK" in f:
        font_manager.fontManager.addfont(f)

matplotlib.rcParams["font.family"] = "sans-serif"
matplotlib.rcParams["font.sans-serif"] = ["Noto Sans CJK SC"]
matplotlib.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("week05/titanic_clean.csv")

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# 图 1：按性别看幸存率
sns.barplot(data=df, x="Sex", y="Survived", ax=axes[0, 0])
axes[0, 0].set_title("性别 vs 幸存率")
axes[0, 0].set_xticklabels(["男", "女"])

# 图 2：按舱位看幸存率
sns.barplot(data=df, x="Pclass", y="Survived", ax=axes[0, 1])
axes[0, 1].set_title("舱位 vs 幸存率")

# 图 3：年龄分布（幸存 vs 未幸存）
sns.histplot(data=df, x="Age", hue="Survived", bins=30, ax=axes[1, 0], multiple="stack")
axes[1, 0].set_title("年龄分布")

# 图 4：相关性热力图
corr = df[["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "FamilySize", "HasCabin"]].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=axes[1, 1], cbar=False)
axes[1, 1].set_title("特征相关性")

fig.suptitle("Titanic 数据分析", fontsize=14)
plt.tight_layout()
fig.savefig("week05/titanic_eda.png", dpi=150, bbox_inches="tight")
print("已保存 week05/titanic_eda.png")
