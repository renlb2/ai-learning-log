import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

# 1. 读取清洗后的数据
df = pd.read_csv("week05/titanic_clean.csv")

# 2. 选几个基础特征（不用 Name/Ticket 这些字符串列）
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "HasCabin"]
X = df[features].copy()
y = df["Survived"]

# ===== 开始特征工程 =====

# 改动 1：交叉特征 (Sex + Pclass)
# 把 Sex(0/1) 和 Pclass(1/2/3) 拼成新特征，比如 male_3 = 3, female_1 = 1
# 公式：新特征 = Sex * 3 + Pclass
X["Sex_Pclass"] = X["Sex"] * 3 + X["Pclass"]

# 改动 2：数值分箱 (Fare)
# 把票价分成 4 份（0, 1, 2, 3），用 pd.qcut
X["Fare_Bin"] = pd.qcut(X["Fare"], q=4, labels=False)

# 改动 3：数值分箱 (Age)
# 按固定区间切分：0-12小孩，12-18少年，18-60成年，60以上老年
bins = [0, 12, 18, 60, 100]
labels = [0, 1, 2, 3]
X["Age_Bin"] = pd.cut(X["Age"], bins=bins, labels=labels)

#改动 4：交叉特征（SibSp + Parch)
#公式：新特征 = SibSp + Parch
X["FamilySize"] = X["SibSp"] + X["Parch"] + 1

# 改动 2：数值分箱 (FamilySize)
# 把家庭规模分成 3 份（0, 1, 2），用 pd.cut
bins =[0,1,3,10]
labels = [0,1,2]
X["Family_Bin"] = pd.cut(X["FamilySize"], bins=bins, labels=labels)

# 把连续变量删掉，只保留分箱后的（树模型更喜欢离散特征）
X = X.drop(columns=["Age", "Fare","FamilySize"])

# =========================

# 3. 模型
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# 4. 交叉验证打分
scores = cross_val_score(rf, X, y, cv=5, scoring="accuracy")
print(f"Baseline 准确率: {scores.mean():.4f} (+/- {scores.std():.4f})")
