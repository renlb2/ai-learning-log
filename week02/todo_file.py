import os

FILE_NAME = "task.txt"


#从文件加载任务

def load_tasks():
	tasks = []
	if os.path.exists(FILE_NAME):
		with open(FILE_NAME,"r",encoding = "utf-8") as f:
			for line in f:
				tasks.append(line.strip())
	return tasks

#保存任务到文件

def save_tasks(tasks):
	with open(FILE_NAME,"w",encoding = "utf-8") as f:
		for task in tasks:
			f.write(task + "\n")

#主程序

tasks = load_tasks()

print("========待办事项（文件版）=========")

while True:
	print("\n1.查看   2.添加   3.删除   4.退出")
	choice = input(">>>")

	if choice == "1":
		if not tasks:
			print("暂无任务")
		else:
			for i,task in enumerate(tasks,start=1):
				print(f"{i}.{task}")
	elif choice == "2":
		new_task = input("新任务：").strip()
		if new_task:
			tasks.append(new_task)
			save_tasks(tasks)
			print("已添加")
	elif choice == "3":
		for i,task in enumerate(tasks,start=1):
			print(f"{i}.{task}")
		index = int(input("删除第几个？"))-1
		if 0<=index<len(tasks):
			removed = tasks.pop(index)
			save_tasks(tasks)
			print(f"已删除{removed}")
		else:
			print("序号无效")
	elif choice == "4":
		print("再见")
		break
	else:
		print("无效选项")

