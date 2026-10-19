from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# 1. 准备数据（注意：这次不用 train_test_split）
X, y = load_iris(return_X_y=True)

# 2. 准备三个模型
models = {
    "逻辑回归": LogisticRegression(max_iter=200),
    "随机森林": RandomForestClassifier(n_estimators=100, random_state=42),
    "KNN (k=3)":KNeighborsClassifier(n_neighbors=3),
    "决策树":   DecisionTreeClassifier(random_state=42),
}

# 3. 对每个模型做 5 折交叉验证
print("=" * 50)
print("5 折交叉验证结果：")
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=10)
    print(f"{name:10s} : 均值 {scores.mean():.4f}  (+/- {scores.std():.4f})")
    print(f"             单次分数: {np.round(scores, 4)}")
