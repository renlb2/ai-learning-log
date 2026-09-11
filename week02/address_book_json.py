import json
import os

FILE_NAME = "contacts.json"

#从文件加载通讯录
def load_contacts():
	if os.path.exists(FILE_NAME):
		with open(FILE_NAME,"r",encoding="utf-8") as f:
			return json.load(f)
	return{}

#保存通讯录到文件
def save_contacts(contcts):
	with open(FILE_NAME,"w",encoding="utf-8") as f:
		json.dump(contacts,f,ensure_ascii=False,indent=4)

#主程序
contacts = load_contacts()

print("==========通讯录（JSON版）==========")

while True:
	print("\n1.添加  2.查找  3.删除  4.查看全部  5.退出")
	choice = input(">>>")

	if choice =="1":
		name = input("姓名：").strip()
		if name in contacts:
			print("该联系人已存在！")
		else:
			phone = input("电话：").strip()
			contacts[name] = phone
			save_contacts(contacts)
			print("已添加")
	elif choice == "2":
		name = input("查找姓名：").strip()
		if name in contacts:
			print(f"{name}:{contacts[name]}")
		else:
			print("查无此人！")
	elif choice == "3":
		name = input("删除姓名：").strip()
		if name in contacts:
			del contacts[name]
			save_contacts(contacts)
			print(f"已删除：{name}")
		else:
			pring("查无此人")
	elif choice == "4":
		if not contacts:
			print("空")
		else:
			for name,phone in contacts.items():
				print(f"{name}:{phone}")
	elif choice == "5":
		print("再见！")
		break
	else:
		print("无效选项")

