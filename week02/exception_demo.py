import os
import json

FILE_NAME = "tasks_safe.json"

def load_tasks():
	if not os.path.exists(FILE_NAME):
		return[]
	try:
		with open(FILE_NAME,"r",encoding = "utf-8") as f:
			return json.load(f)
	except json.JSONDecodeError:
		print("文件损坏，已重置为空列表")
		return []
	except Exception as e:
		print(f"读取失败：{e}")
		return []

def save_tasks(tasks):
	try:
		with open(FILE_NAME,"w",encoding="utf-8") as f:
			json.dump(tasks,f,ensure_ascii=False,indent=4)
		print("已保存")
	except Exception as e:
		print(f"保存失败：{e}")

#主程序

tasks = load_tasks()
print("==========待办事项（异常处理版）==========")

while True:
	print("\n1.查看  2.添加  3.删除  4.退出")
	try:
		choice =input( ">>>>>")
	except (EOFError,KeyboardInterrupt):
		print("\n再见")
		break

	if choice == "1":
		if not tasks:
			print("暂无任务")
		else:
			for i,task in enumerate(tasks,start=1):
				print(f"{i}.{task}")
	elif choice == "2":
		task = input("新任务：").strip()
		if task:
			tasks.append(task)
			save_tasks(tasks)
		else:
			print("任务不能为空")
	elif choice == "3":
		if not tasks:
			print("没有可删除的任务")
			continue
		for i ,task in enumerate(tasks,start=1):
			print(f"{i}.{task}")
		try:
			index = int(input("删除第几个："))-1
			if 0<= index <len(tasks):
				removed = tasks.pop(index)
				print(f"已删除{removed}")
			else:
				print("序号无效")
		except ValueError:
			print("请输入数字")
	elif choice == "4":
		print("再见")
		break

	else:
		print("无效选项")
