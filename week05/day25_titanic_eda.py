import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "WenQuanYi Micro Hei"]
matplotlib.rcParams["axes.unicode_minus"] = False
sns.set_theme(style="whitegrid")

# ===== 第 1 步：加载数据 =====
df = pd.read_csv("week05/titanic.csv")

print("=" * 50)
print("shape:", df.shape)
print("\n前 5 行：")
print(df.head())

print("\n数据信息：")
df.info()

# ===== 第 2 步：看目标变量 =====
# TODO 1：Survived 的比例分布
survived_ratio = df["Survived"].value_counts(normalize=True)
print("\n幸存比例：")
print(survived_ratio)

# ===== 第 3 步：缺失值 =====
# TODO 2：每列缺失数，按从多到少排
missing = df.isnull().sum().sort_values(ascending=False)
print("\n缺失值：")
print(missing[missing > 0])

# ===== 第 4 步：单变量分析 =====
# TODO 3：按 Sex 看幸存率
survived_by_sex = df.groupby("Sex")["Survived"].mean()

# TODO 4：按 Pclass 看幸存率
survived_by_pclass = df.groupby("Pclass")["Survived"].mean()

# TODO 5：按 ["Sex", "Pclass"] 两个变量交叉看幸存率
survived_by_both = df.groupby(["Sex","Pclass"])["Survived"].mean()

print("\n按性别：")
print(survived_by_sex)
print("\n按舱位：")
print(survived_by_pclass)
print("\n按性别+舱位：")
print(survived_by_both)

# ===== 第 5 步：清洗 =====
# 5.1 填充 Age：按 Sex + Pclass 分组，用中位数填
# TODO 6：用 groupby transform 填 Age
df["Age"] = df.groupby(["Sex","Pclass"])["Age"].transform(lambda x:x.fillna(x.median()))

# 5.2 Cabin：造一个 HasCabin 列，然后删掉原 Cabin 列
# TODO 7：HasCabin = Cabin 不为空
df["HasCabin"] = df["Cabin"].notnull()
df = df.drop(columns=["Cabin"])

# 5.3 Embarked：用众数填
# TODO 8：用众数填 Embarked
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# ===== 第 6 步：特征工程 =====
# TODO 9：FamilySize = SibSp + Parch + 1
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# TODO 10：IsAlone = FamilySize == 1
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

# TODO 11：从 Name 提取 Title
df["Title"] = df["Name"].str.extract(r" ([A-Za-z]+)\.",expand=False)

print("\nTitle 分布：")
print(df["Title"].value_counts())

# ===== 第 7 步：处理类别变量 =====
# TODO 12：把 Sex 映射成 male=0, female=1
df["Sex"] = df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

# TODO 13：把 Embarked 映射成 S=0, C=1, Q=2
df["Embarked"] = df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

# TODO 14：Title 里罕见的合并成 Rare，然后映射
rare_titles = ["Lady","Countess","Capt","Col","Don","Dr","Major","Rev","Sir","Jonkheer","Dona"]
df["Title"] = df["Title"].replace(rare_titles, "Rare")
df["Title"] = df["Title"].map({"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5,    "Mlle": 2,    # 法语 Miss
    "Mme": 3,     # 法语 Mrs
    "Ms": 2,      # 英语 Miss 的变体
})
df["Title"] = df["Title"].fillna(5).astype(int)

# ===== 第 8 步：保存清洗后的数据 =====
df.to_csv("week05/titanic_clean.csv", index=False, encoding="utf-8-sig")
print("\n已保存 week05/titanic_clean.csv")
print("清洗后 shape:", df.shape)
print("清洗后还有缺失：")
print(df.isnull().sum()[df.isnull().sum() > 0])



print(df[df["Title"].isnull()][["Name"]])
