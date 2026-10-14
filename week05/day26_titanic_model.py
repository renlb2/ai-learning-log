import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ===== 第 1 步：读清洗后的数据 =====
df = pd.read_csv("week05/titanic_clean.csv")

# 删掉不需要做特征的列
drop_cols = ["PassengerId", "Name", "Ticket"]
# TODO 1：删掉这三列
df = df.drop(columns=drop_cols)

print("数据 shape:", df.shape)
print("列名:", list(df.columns))

# ===== 第 2 步：定义 X 和 y =====
# TODO 2：y = Survived 列
y = df["Survived"]

# TODO 3：X = 除了 Survived 之外的所有列
X = df.drop(columns=["Survived"])

# 保险：把布尔列转成 0/1（HasCabin）
X["HasCabin"] = X["HasCabin"].astype(int)

print("\nX shape:", X.shape)
print("y shape:", y.shape)
print("X 列:", list(X.columns))

# ===== 第 3 步：划分训练 / 测试 =====
# TODO 4：80% 训练，20% 测试，random_state=42，stratify=y
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

print(f"\n训练集: {X_train.shape[0]} 行, 测试集: {X_test.shape[0]} 行")

# ===== 第 4 步：逻辑回归 =====
# TODO 5：建 LogisticRegression，max_iter=1000
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_acc = accuracy_score(y_test, lr_pred)

print("\n" + "=" * 50)
print(f"逻辑回归 准确率: {lr_acc:.4f}")
print("混淆矩阵：")
print(confusion_matrix(y_test, lr_pred))
print("\n分类报告：")
print(classification_report(y_test, lr_pred))

# ===== 第 5 步：随机森林 =====
# TODO 6：建 RandomForestClassifier，n_estimators=100，random_state=42
rf = RandomForestClassifier(n_estimators=100,random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)

print("\n" + "=" * 50)
print(f"随机森林 准确率: {rf_acc:.4f}")
print("混淆矩阵：")
print(confusion_matrix(y_test, rf_pred))
print("\n分类报告：")
print(classification_report(y_test, rf_pred))

# ===== 第 6 步：交叉验证（更稳） =====
# TODO 7：对逻辑回归做 5 折交叉验证
lr_cv = cross_val_score(lr,X,y,cv=5,scoring="accuracy")
print("\n" + "=" * 50)
print(f"逻辑回归 5 折 CV: {lr_cv.mean():.4f} (+/- {lr_cv.std():.4f})")

# TODO 8：对随机森林做 5 折交叉验证
rf_cv = cross_val_score(rf,X,y,cv=5,scoring="accuracy")
print(f"随机森林 5 折 CV: {rf_cv.mean():.4f} (+/- {rf_cv.std():.4f})")

# ===== 第 7 步：选更好的模型，生成提交文件 =====
best_model = rf if rf_acc > lr_acc else lr
best_name = "随机森林" if rf_acc > lr_acc else "逻辑回归"
print(f"\n最佳模型：{best_name}")

# 用最佳模型预测测试集，生成演示提交文件
demo_submission = pd.DataFrame({
    "PassengerId": df.loc[X_test.index, "PassengerId"] if "PassengerId" in df.columns else X_test.index,
    "Survived": best_model.predict(X_test)
})
demo_submission.to_csv("week05/submission_demo.csv", index=False)
print(f"已保存 week05/submission_demo.csv ({len(demo_submission)} 行)")
print(demo_submission.head())

# ===== 第 8 步：特征重要性（随机森林专属） =====
print("\n" + "=" * 50)
print("随机森林特征重要性（前 10）：")
importance = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
print(importance.head(10))
