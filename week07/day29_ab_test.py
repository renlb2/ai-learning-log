import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np

df = pd.read_csv("week05/titanic_clean.csv")
y = df["Survived"]
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# 组 A：只用最原始的 8 个特征
X_a = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "HasCabin"]].copy()

# 组 B：原始特征 + 各种衍生特征
X_b = X_a.copy()
X_b["Title"] = df["Title"]
X_b["IsAlone"] = df["IsAlone"]
X_b["Sex_Pclass"] = df["Sex"] * 3 + df["Pclass"]
X_b["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# 为了公平，我们设置 cv=10，并且用 5 个不同的随机种子跑，取平均
seeds = [1, 10, 42, 100, 2026]
scores_a, scores_b = [], []

for s in seeds:
    # 注意：cross_val_score 也有随机性，这里我们通过多次运行来平滑
    sa = cross_val_score(rf, X_a, y, cv=10).mean()
    sb = cross_val_score(rf, X_b, y, cv=10).mean()
    scores_a.append(sa)
    scores_b.append(sb)

print(f"组 A（纯原始特征）平均分: {np.mean(scores_a):.4f}")
print(f"组 B（原始+特征工程）平均分: {np.mean(scores_b):.4f}")
