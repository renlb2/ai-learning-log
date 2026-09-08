#BMI 计算器

#公式：BMI = 体重 / （身高 × 身高 ）

name = input ("请输入你的名字：")

height = float(input("请输入你的身高（米）："))

weight = float(input("请输入你的体重（公斤）："))

bmi = weight / (height ** 2)

print(f"\n{name}，你的 BMI 是：{bmi: .2f}")

#判断体型

if bmi < 18.5:
	print("你偏瘦，多吃点！")
elif bmi < 24:
	print("你的体重正常，继续保持！")
elif bmi > 28:
	print("你超重了，注意控制饮食！")
else:
	print("你肥胖，建议咨询医生或营养师！")
