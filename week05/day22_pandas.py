import pandas as pd

#=====第一步：建数据=====
data = {
    "name":   ["小明","小红","小刚","小美","小强","小丽"],
    "math":   [85,92,78,95,60,88],
    "english":[88,95,80,92,72,85],
    "physics":[80,90,75,96,65,82],
}

df = pd.DataFrame(data)

#=====第 2 步：看数据=====
print("=" * 40)
print("前 3 行：")
print(df.head(3))

print("\n数据信息：")
df.info()

print("\n数值列统计：")
print(df.describe())

print("\nshape：",df.shape)

#=====第 3 步：新增列=====)
#TODO 1： 新增total列 = 三科之和
df["total"] = df["math"] + df["english"] + df["physics"]

#TODO 2：新增 avg 列 = 三科平均
df["avg"] = df["total"] / 3

#TODO 3 :新增pass列 = avg >= 60的布尔值
df["pass"] = df["avg"] >= 60

print("\n加列后：")
print(df)

#=====第 4 步：选列选行=====
#TODO 4：用loc取第 0 行的math列
first_math = df.loc[0,"math"]

#TODO 5：用iloc取第 0 行第 1 列
first_math_iloc = df.iloc[0,1]

#TODO 6 ：取前 3 行的name和math两列
sub_table = df.loc[0:2,["name","math"]]

print("\n第一个学生数学(loc)：",first_math)
print("第一个学生数学(iloc)：",first_math_iloc)
print("\n前 3 行name+math：")
print(sub_table)

#=====第 5 步：条件筛选=====
#TODO 7：筛选出数学 > 85的学生
high_math = df[df["math"] > 85]

#TODO 8：筛选出数学 > 85 且英语 > 90的学生
high_both = df[(df["math"] > 85) & (df["english"] > 90)]

print("\n数学 > 85 的学生：")
print(high_math[["name","math"]])

print("\n数学 > 85 且 英语 > 90 的学生：")
print(high_both[["name","english","math"]])

#=====第 6 步：排序=====
#TODO 9：按total降序排序
sorted_df = df.sort_values("total",ascending=False)

print("\n按总分降序：")
print(sorted_df[["name","total","avg"]])

#=====第 7 步：读写 CSV =====
df.to_csv("week05/scores.csv",index=False,encoding="utf-8-sig")
print("\n已写出week05/scores.csv")

#读回来验证
df2 = pd.read_csv("week05/scores.csv")
print("\n从 CSV 读回来的 shape:",df2.shape)
print(df2.head())
