# Day 23 - pandas 进阶

## 核心知识点
- groupby：split-apply-combine
- 聚合：mean / sum / max / count / agg(["mean","max","min"])
- 缺失值检测：isnull().sum()
- 缺失值处理：dropna / fillna(均值)
- merge：inner / left / right / outer
- pivot_table：Excel 透视表的 pandas 版

## 产出
- week05/day23_pandas.py

## 验证结果
- 缺失值：math 1 个、english 1 个，用均值填充
- 按班级 total 平均：A 班 170.5，B 班 163.5
- merge 后 7 行 7 列
- 按性别分组：
  F math 91.67 / english 87.17
  M math 74.75 / english 82.50

## 数据洞察
- 女生数学平均比男生高 16.9 分，英语高 4.67 分
- 样本量小（女 3 人、男 4 人），结论仅供参考，不能推广

## 踩坑
- df.merge(df, info, ...) 传了两个位置参数，报 "multiple values for argument 'how'"
  原因：DataFrame.merge 只接收一个位置参数（另一张表）
  正确：df.merge(info, on="name", how="left") 或 pd.merge(df, info, ...)
