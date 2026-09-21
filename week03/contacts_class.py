import json
import os

FILE_NAME = "contacts_class.json"

class Contact:
	"""联系人基类"""
	def __init__(self,name,phone):
		if not name:
			raise ValueError("姓名不能为空")
		if not phone or not phone.replace("-","").isdigit():
			raise ValueError("电话必须是数字")
		self.name = name
		self.phone = phone
	def info(self):
		return f"{self.name}：{self.phone}"
	def to_dict(self):
		return {"type":"contact","name":self.name,"phone":self.phone}
	@classmethod
	def from_dict(cls,d):
		return cls(d["name"],d["phone"])
	def __str__(self):
		return self.info()

class PersonalContact(Contact):
	"""个人联系人"""
	def __init__(self,name,phone,birthday,relation):
		super().__init__(name,phone)
		self.birthday = birthday
		self.relation = relation
	def info(self):
		return f"{self.name}：{self.phone}|生日：{self.birthday}关系：{self.relation}"
	def to_dict(self):
		d = super().to_dict()
		d["type"] = "personal"
		d["birthday"] = self.birthday
		d["relation"] = self.relation
		return d
	@classmethod
	def from_dict(cls,d):
		return cls(d["name"],d["phone"],d["birthday"],d["relation"])

class BusinessContact(Contact):
	"""商务联系人"""
	def __init__(self,name,phone,company,title):
		super().__init__(name,phone)
		self.company = company
		self.title = title
	def info(self):
		return f"{self.name}：{self.phone}|公司：{self.company}职位：{self.title}"
	def to_dict(self):
		d = super().to_dict()
		d["type"] = "business"
		d["company"] = self.company
		d["title"] = self.title
		return d
	@classmethod
	def from_dict(cls,d):
		return cls(d["name"],d["phone"],d["company"],d["title"])

class ContactManager:
	"""联系人管理器"""
	def __init__(self):
		self.contacts = []
	def add_contact(self,contact):
		self.contacts.append(contact)
		print(f"已添加：{contact.name}")
	def show_contacts(self):
		if not self.contacts:
			print("（暂无联系人）")
			return
		for i,c in enumerate(self.contacts,1):
			print(f"{i}.{c.info()}")
	def find_contact(self,name):
		for c in self.contacts:
			if c.name == name:
				return c
		return None
	def delete_contact(self,index):
		if 1 <= index <= len(self.contacts):
			removed = self.contacts.pop(index - 1)
			print(f"已删除：{removed.name}")
		else:
			print("无效编号")
	def save(self):
		try:
			with open(FILE_NAME,"w",encoding = "utf-8") as f:
				json.dump([c.to_dict() for c in self.contacts],f,ensure_ascii = False,indent = 4)
		except Exception as e:
			print(f"保存失败：{e}")
	def load(self):
		if not os.path.exists(FILE_NAME):
			return
		try:
			with open(FILE_NAME,"r",encoding = "utf-8") as f:
				data = json.load(f)
			if isinstance(data,list):
				self.contacts = []
				for d in data:
					ctype = d.get("type","contact")
					if ctype == "personal":
						self.contacts.append(PersonalContact.from_dict(d))
					elif ctype == "business":
						self.contacts.append(BusinessContact.from_dict(d))
					else:
						self.contacts.append(Contact.from_dict(d))
			else:
				print("数据格式异常，已重置")
				self.contacts = []
		except json.JSONDecodeError:
			print(f"文件损坏，已重置")
			self.contacts = []
		except Exception as e:
			print(f"读取失败：{e}")
			self.contacts = []

def main():
	manager = ContactManager()
	manager.load()
	print("==========通讯录（class版 + 继承）==========")

	while True:
		print("\n1.查看  2.添加个人  3.添加商务  4.查找  5.删除  6.保存退出")
		try:
			choice = input(">>>>>>").strip()
		except (EOFError, KeyboardInterrupt):
			manager.save()
			print("\n已保存，再见")
			break

		if choice == "1":
			manager.show_contacts()
		elif choice in ("2","3"):
			name = input("姓名：").strip()
			phone = input("电话：").strip()
			if not name or not phone:
				print("姓名和电话不能为空")
				continue
			if choice == "2":
				birthday = input("生日：").strip()
				relation = input("关系：").strip()
				try:
					contact = PersonalContact(name,phone,birthday,relation)
					manager.add_contact(contact)
				except ValueError as e:
					print(f"添加失败：{e}")
			else:
				company = input("公司：").strip()
				title = input("职务：").strip()
				try:
					contact = BusinessContact(name,phone,company,title)
					manager.add_contact(contact)
				except ValueError as e:
					print(f"添加失败：{e}")
		elif choice == "4":
			name = input("查找姓名：").strip()
			result = manager.find_contact(name)
			if result:
				print(result.info())
			else:
				print("未找到")
		elif choice == "5":
			manager.show_contacts()
			try:
				idx = int(input("删除第几个："))
				manager.delete_contact(idx)
			except ValueError:
				print("请输入数字")
		elif choice == "6":
			manager.save()
			print("已保存，再见")
			break
		else:
			print("无效选项")


if __name__ == "__main__":
	main()
