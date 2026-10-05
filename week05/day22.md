# Day 22 - pandas 入门

## 核心知识点
- Series：带索引的一维数据
- DataFrame：带行列标签的二维表
- 建表：pd.DataFrame(dict)
- 读写：read_csv / to_csv(index=False, encoding="utf-8-sig")
- 看数据三件套：head / info / describe
- 选列：df["col"] / df[["c1", "c2"]]
- loc（标签）vs iloc（位置）
- 条件筛选：df[df["x"] > 0]，多条件用 & | 且加括号
- 新增列：df["new"] = df["a"] + df["b"]
- 排序：sort_values("col", ascending=False)

## 产出
- week05/day22_pandas.py
- week05/scores.csv

## 验证结果
- 6 名学生，3 科成绩，加 3 列后 7 列
- 数学 > 85：3 人
- 数学 > 85 且 英语 > 90：2 人
- 排序正确，CSV 读回 shape 一致

## 踩坑
- df[["name"],["math"]] 多了方括号，pandas 把它当元组 → InvalidIndexError
  正确写法：df[["name", "math"]]（列表套列表，逗号在同一层）
- pass 是 Python 关键字，df["pass"] 能用但 df.pass 会 SyntaxError，建议改名 passed

## 明天（Day 23）
pandas 进阶：groupby / 缺失值处理 / merge
