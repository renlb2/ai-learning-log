import random


secret = random.randint(1,100)
attempts = 0

print("我想了一个1到100之间的数字，你来猜！")


while True:
		
	#限制最多猜7次
	if attempts >= 7:
		
		print(f"次数用完了！，答案是{secret}。")
		break



	guess = int(input("请输入你的猜测："))
	attempts =attempts + 1


	if guess < secret:
		print("往大了猜！")
	elif guess > secret:
		print("往小了猜！")
	else:
		print(f"恭喜你，猜对了！答案是{secret}！")
		print(f"你一共猜了{attempts}次。")
		break

