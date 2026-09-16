import os
import json

FILE_NAME = "contacts_final.json"

#加载通讯录

def load_contacts():
	if not os.path.exists(FILE_NAME):
		return{}
	try:
		with open(FILE_NAME,"r",encoding = "utf-8") as f:
			data = json.load(f)
			if isinstance(data,dict):
				return(data)
			else:
				print("数据格式异常，已重置为空通讯录")
				return{}
	except json.JSONDecodeError:
		print("文件损坏，已重置为空通讯录")
		return{}
	except Exception as e:
		print(f"读取失败：{e}“")
		return{}

#保存通讯录

def save_contacts(contacts):
	try:
		with open(FILE_NAME,"w",encoding = "utf-8") as f:
			json.dump(contacts,f,ensure_ascii = False,indent = 4)
	except Exception as e:
			pring(f"保存失败： {e}")

#主程序

contacts = load_contacts()
print("==========通讯录（最终版）==========")

while True:
	print("\n1.查看  2.添加  3.查找  4.删除  5.退出")
	try:
		choice = input(">>>>>").strip()
	except (EOFError,KeyboardInterrupt):
		print("\n再见！")
		break

	if choice == "1":
		if not contacts:
			print("(暂无联系人)")
		else:
			for name,phone in contacts.items():
				print(f"{name}.{phone}")

	elif choice == "2":
		name = input("姓名：").strip()
		phone = input("电话：").strip()
		if name and phone:
			contacts[name] = phone
			save_contacts(contacts)
			print("已添加")
		else:
			print("姓名和电话不能为空")
	elif choice == "3":
		name = input("查找姓名：").strip()
		if name in contacts:
			print(f"{name}.{contacts[name]}")
		else:
			print("未找到联系人")
	elif choice == "4":
		name = input("删除姓名：").strip()
		if name in contacts:
			removed_phone = contacts.pop(name)
			save_contacts(contacts)
			print(f"已删除，{name}({removed_phone})")
		else:
			print("未找到该联系人")
	elif choice == "5":
		print("再见！")
		break
	else:
		print("无效选项，请重新输入")
