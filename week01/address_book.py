#用字典存储联系人：姓名 ->电话
contacts = {}

def add_contacts():
	name = input("请输入姓名：").strip()
	if name in contacts:
		print("改联系人已存在")
		return
	phone = input("请输入电话：").strip()
	contacts[name] = phone
	print(f"已添加：{name}->{phone}")

def search_contacts():
	name = input("请输入要查找的姓名：").strip()
	if name in contacts:
		print(f"{name}:{contacts[name]}")
	else:
		print("查无此人。")

def delete_contacts():
	name = input("请输入要删除的姓名：").strip()
	if name in contacts:
		del contacts[name]
		print(f"已删除：{name}")
	else:
		print("查无此人。")

def  show_all():
	if len(contacts) ==0:
		print("通讯录为空")
		return
	print("==========通讯录==========")
	for name,phone in contacts.items():
		print(f"{name}:{phone}")
	print("==========================")


#主程序

print("==========简易通讯录==========")
while  True:
	print("\n请选择操作：")
	print("1.添加联系人：")
	print("2.查找联系人：")
	print("3.删除联系人：")
	print("4.查看全部")
	print("5.退出")

	choice = input("输入选项（1-5）。")

	if choice == "1":
		add_contacts()
	elif choice == "2":
		search_contacts()
	elif choice == "3":
		delete_contacts()
	elif choice == "4":
		show_all()
	elif choice == "5":
		print("再见！")
		break
	else:
		print("无效选项，请输入1-5。")
