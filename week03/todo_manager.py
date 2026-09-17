import os
import json

FILE_NAME = "tasks_class.json"

class Task:
	"""单个待办事项"""
	def __init__(self,name):
		self.name = name
		self.done = False
	
	def mark_done(self):
		self.done = True

	def mark_undone (self):
		self.done = False
	def to_dict(self):
		"""转成字典，方便存JSON"""
		return {"name":self.name,"done":self.done}
	@classmethod
	def from_dict(cls,d):
		"""从字典创建Task对象"""
		task = cls(d["name"])
		task.done = d["done"]
		return task
	def __str__(self):
		status = "✅" if self.done else "❌"
		return f"{status}{self.name}"
class TodoManager:
	"""待办管理器"""
	def __init__(self):
		self.tasks = []
	def add_task(self,name):
		task = Task(name)
		self.tasks.append(task)
		print(f"已添加：{name}")
	def show_tasks(self):
		if not self.tasks:
			print("（暂无任务）")
			return
		for i,task in enumerate(self.tasks,1):
			print(f"{i}.{task}")
	def mark_done(self,index):
		if 1 <= index <= len(self.tasks):
			self.tasks[index - 1].mark_done()
			print(f"已标记完成：{self.tasks[index-1].name}")
		else:
			print("无效编号")
	def delete_task(self,index):
		if 1 <= index <=len(self.tasks):
			removed = self.tasks.pop(index - 1)
			print(f"已删除：{removed.name}")
		else:
			print("无效编号")
	def save(self):
		"""保存到JSON文件"""
		try:
			with open(FILE_NAME,"w",encoding = "utf-8") as f:
				json.dump([t.to_dict() for t in self.tasks],f,ensure_ascii = False,indent = 4)
		except Exception as e:
			print(f"保存失败：{e}")

	def load(self):
		"""从JSON文件加载"""
		if not os.path.exists(FILE_NAME):
			return
		try:
			with open(FILE_NAME,"r",encoding = "utf-8") as f:
				data = json.load(f)
			if isinstance(data,list):
				self.tasks = [Task.from_dict(d) for d in data]
			else:
				print("数据格式异常，已重置")
		except json.JSONDecodeError:
                        print("文件损坏，已重置")

		except Exception as e:
			print(f"读取失败：{e}")

#主程序
def main():
	manager = TodoManager()
	manager.load()
	print("==========待办管理器（class版）==========")
	
	while True:
		print("\n1. 查看  2.添加  3.标记完成  4.删除  5.保存退出")
		try:
			choice = input(">>>>>").strip()
		except (EOFError,KeyboardInterrupt):
			manager.save()
			print("\n已保存，再见！")
			break
		if choice == "1":
			manager.show_tasks()
		elif choice == "2":
			name = input("任务名：").strip()
			if name:
				manager.add_task(name)
			else:
				print("任务名不能为空")
		elif choice == "3":
			manager.show_tasks()
			try:
				idx = int(input("标记第几个："))
				manager.mark_done(idx)
			except ValueError:
				print("请输入数字")
		elif choice == "4":
			manager.show_tasks()
			try:
				idx = int(input("删除第几个："))
				manager.delete_task(idx)
			except ValueError:
				print("请输入数字")
		elif choice == "5":
			manager.save()
			print("已保存，再见！")
			break
		else:
			print("无效选项")
if __name__ == "__main__":
	main()
