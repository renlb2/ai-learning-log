import pandas as pd
import numpy as np

#=====第 1 步：建一个有缺失值和分组的表=====
df = pd.DataFrame({
    "class":  ["A","A","A","B","B","B","B"],
    "name":   ["小明","小红","小刚","小美","小强","小丽","小华"],
    "math":   [85,92,None,95,60,88,72],
    "english":[88,None,80,92,72,85,90],
})

print("=" * 40)
print("原始数据：")
print(df)

#=====第 2 步：检查缺失值=====
#TODO 1：每列有几个NaN
missing_count = df.isnull().sum()

print("\n每列缺失值数量：")
print(missing_count)

#TODO 2 ：只看math缺失的行
missing_math = df[df["math"].isnull()]
print("\nmath缺失的行：")
print(missing_math[["class","name","math"]])

#=====第 3 步 ：填充缺失值=====
#TOTO 3 ：用math列的平均值填math的NaN
df["math"] = df["math"].fillna(df["math"].mean())

#TODO 4 :用english列的平均值填english的NaN
df["english"] = df["english"].fillna(df["english"].mean())

print("\n填充后：")
print(df)

#=====第 4 步：新增列=====
#TODO 5 :新增total = math + english
df["total"] = df["math"] + df["english"]

#TODO 6 ：新增avg列
df["avg"] = df["total"] / 2

#=====第 5 步：groupby分组统计
#TODO 7：按class分组，算math的平均值
math_by_math = df.groupby("class")["math"].mean()

#TODO 8 ：按class分组，算total的平均值 + 最大 + 最小
total_by_class = df.groupby("class")["total"].agg(["mean","max","min"])

print("\n按班级算total平均/最大/最小：")
print(total_by_class)

#=====第 6 步：merge合并另一张表=====
#学生信息表（含性别）
info = pd.DataFrame({
    "name":["小明","小红","小刚","小美","小强","小丽","小华"],
    "gender":["M","F","M","F","M","F","M"],
})

#TODO 9 ：把df和info按name合并（左连接）
merged = pd.merge(df,info,on="name",how="left")

print("\n合并后：")
print(merged)

#TODO 10 ：按gender分组，算math和english的平均分
gender_avg = merged.groupby("gender")[["math","english"]].mean()

print("\n按性别算：math和english平均：")
print(gender_avg)
