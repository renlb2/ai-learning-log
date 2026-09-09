tasks = []


print("================待办事项管理器===============")

while True:
	print("\n请选择操作：")
	print("1. 查看任务")
	print("2. 添加任务")
	print("3. 删除任务")
	print("4. 退出")


	choice = input("输入选项（1-4）：")

	if choice == "1":

		#添加任务
		if len(tasks) == 0:
			print("（暂无任务）")
		else:
			for i,task in enumerate(tasks):
				print(f"{i+1}.{task}")

	elif choice == "2":
		#添加任务
		new_task = input("请输入新任务：").strip()
		if new_task:
			tasks.append(new_task)
			print(f"已添加：{new_task}")
		else:
			print("任务不能为空")

	elif  choice == "3":
		#删除任务
		if len(tasks) == 0:
			print("（暂无任务可删除）")
			continue
		for i, task in enumerate(tasks):
			print(f"{i+1}.{task}")
		index = int(input("要删除第几个？"))-1
		if 0 <= index <len(tasks):
			remove = tasks.pop(index)
			print(f"已删除：{remove}")
		else:
			print("序号无效")
	elif choice == "4":
		#退出
		print("再见")
		break
	else:
		print("无效选项，请输入1-4。")
