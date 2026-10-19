import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("week05/titanic_clean.csv")

# 注意：把 Title 和 IsAlone 加回来！
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "HasCabin", "Title", "IsAlone"]
X = df[features].copy()
y = df["Survived"]

# ===== 特征工程 =====

# 1. 交叉特征
X["Sex_Pclass"] = X["Sex"] * 3 + X["Pclass"]

# 2. 家庭规模（你的加1版本）
X["FamilySize"] = X["SibSp"] + X["Parch"] + 1

# 3. 提取衍生特征，但【不删除】原始的 Age 和 Fare
X["Age_Bin"] = pd.cut(X["Age"], bins=[0, 12, 18, 60, 100], labels=[0, 1, 2, 3])
X["Family_Bin"] = pd.cut(X["FamilySize"], bins=[0, 1, 3, 10], labels=[0, 1, 2])

# 把中间计算用的 FamilySize 删掉，但保留原始 SibSp 和 Parch
X = X.drop(columns=["FamilySize"])

# ===== 模型 =====
rf = RandomForestClassifier(n_estimators=100, random_state=42)
scores = cross_val_score(rf, X, y, cv=5, scoring="accuracy")
print(f"终极版准确率: {scores.mean():.4f} (+/- {scores.std():.4f})")
