from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

X, y = load_iris(return_X_y=True)

# 1. 定义要试的参数范围
param_grid = {
    "n_neighbors": [1, 3, 5, 7, 9, 11]
}

# 2. 建一个基础模型
knn = KNeighborsClassifier()

# 3. 网格搜索：自动试 6 个 k 值，每个做 5 折 CV
grid = GridSearchCV(knn, param_grid, cv=5, scoring="accuracy")
grid.fit(X, y)

# 4. 看结果
print("=" * 50)
print("最佳参数:", grid.best_params_)
print(f"最佳 CV 分数: {grid.best_score_:.4f}")

# 5. 看每个 k 对应的分数（看趋势）
import pandas as pd
results = pd.DataFrame(grid.cv_results_)
print("\n每个 k 的分数：")
print(results[["param_n_neighbors", "mean_test_score", "std_test_score"]])
