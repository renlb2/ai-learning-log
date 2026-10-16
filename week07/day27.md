# Day 27 - sklearn 四步走（读-改-写）

## 四步骨架
1. 准备数据：X + y
2. 划分：train_test_split(test_size=0.2, stratify=y)
3. 训练：model.fit(X_train, y_train)
4. 评估：model.predict(X_test) → accuracy / classification_report

## 今天跑了三个数据集
- iris + 逻辑回归：0.9667
- digits + 逻辑回归：0.9611
- iris + KNN：1.0000

## 观察
- digits 里 8 和 9 最容易错（recall 最低）
- iris 上 KNN 全对，因为数据太简单 + setosa 线性可分
- 1.0 不代表模型强，真实数据不会这么干净

## 踩坑


## 明天（Day 28）
交叉验证 + 模型调参入门
