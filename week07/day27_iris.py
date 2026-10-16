from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. 加载数据
iris = load_iris()
X = iris.data 
y = iris.target

print("X shape:", X.shape)
print("y 类别:", set(y))
print("特征名:", iris.feature_names)
print("类别名:", iris.target_names)

# 2. 划分训练/测试
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. 训练模型
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# 4. 评估
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\n准确率: {acc:.4f}")
print("\n分类报告：")
print(classification_report(y_test, y_pred,target_names=iris.target_names))

from sklearn.metrics import confusion_matrix
print("\n混淆矩阵：")
print(confusion_matrix(y_test, y_pred))
