from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

X, y = load_iris(return_X_y=True)

# 1. 定义要试的参数范围
param_grid = {
    "n_estimators": [10, 50, 100, 200]
}

# 2. 建一个基础模型
RF = RandomForestClassifier()

# 3. 网格搜索：自动试 6 个 k 值，每个做 5 折 CV
grid = GridSearchCV(RF, param_grid, cv=5, scoring="accuracy")
grid.fit(X, y)

# 4. 看结果
print("=" * 50)
print("最佳参数:", grid.best_params_)
print(f"最佳 CV 分数: {grid.best_score_:.4f}")

# 5. 看每个 k 对应的分数（看趋势）
import pandas as pd
results = pd.DataFrame(grid.cv_results_)
print("\n每个 k 的分数：")
print(results[["param_n_estimators", "mean_test_score", "std_test_score"]])
