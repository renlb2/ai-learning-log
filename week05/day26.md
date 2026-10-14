# Day 26 - Titanic 建模 + 提交

## 核心知识点
- ML 框架：X + y → 模型 → 预测
- train_test_split(test_size=0.2, stratify=y)
- 基线模型：LogisticRegression / RandomForestClassifier
- 评估：accuracy / confusion_matrix / classification_report
- 交叉验证：cross_val_score(cv=5)，比单次划分稳
- 特征重要性：rf.feature_importances_
- submission.csv 格式：PassengerId + Survived

## 结果
- 逻辑回归 单次 0.7933 / CV 0.8148
- 随机森林 单次 0.7989 / CV 0.8069
- 结论：CV 里 LR 更好，应选 LR 作为最佳模型
- 特征重要性：Fare > Age > Title > Sex > Pclass

## 踩坑与观察
1. 单次划分有随机性，CV 更可信；选模型要看 CV 不看单次
2. Sex 在 EDA 里最强，但 RF 重要性排第 4
   原因：连续变量(Fare)有更多切分点，容易刷高重要性
   更严谨的方法：permutation importance
3. 混淆矩阵 RF：FN 19（活人误判为死）比 FP 17 更值得关注
   如果实际场景重视召回率，可以调阈值

## 产出
- week05/day26_titanic_model.py
- week05/submission_demo.csv（179 行）

## Week 05 完成
- Day 21-26 走通一个完整 ML 项目：数据 → 清洗 → 特征 → 模型 → 评估 → 提交
