import numpy as np

#5名学生，4门课的成绩（行=学生，列=科目）
#科目顺序：语文、数学、英语、物理
scores = np.array([
    [85,92,78,88],
    [70,65,80,72],
    [95,98,92,96],
    [60,72,68,75],
    [88,85,90,92],
])

print("成绩表 shape:",scores.shape)

#TODO 1:计算每个学生的总分（每人4科之和）
#提示：用axis=1
student_total = scores.sum(axis=1)

#TODO 2：计算每门课的平均分
#提示：用axis=0
subject_mean = scores.mean(axis=0)

#TODO 3：找出总分最高的学生索引（0-based)
#提示：用np.argmax
top_student = np.argmax(student_total)

#TODO 4：计算班级总平均分（所有成绩的平均）
class_mean = scores.mean()

#TODO 5：筛选出所有 >=90的成绩
high_scores = scores[scores > 90]

#TODO 6：吧每个学生的分数都加5分（加分政策）
#提示：scores + 5,赋值给变量
boosted = scores + 5

#-----打印结果-----
print("\n每个学生总分：",student_total)
print("\n每门课平均分：",subject_mean)
print("\n总分最高的学生索引：",top_student)
print("\n班级总平均分：",round(class_mean,2))
print("\n所有 >= 90的成绩：",high_scores)
print("\n加5分后第一行：",boosted[0])
print("\n原数组第一行（应不变）：",scores[0])

