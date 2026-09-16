class Task:
	"""待办事项类"""
	def __init__(self,name):
		self.name = name
		self.done = False

	def mark_done(self):
		self.done = True

	def mark_undone(self):
		self.done = False

	def __str__(self):
		status = "✅" if self.done else "❌"
		return f"{status}{self.name}"

if __name__ == "__main__":
	print("==========测试Task类==========")
	t1 = Task("跑步")
	t2 = Task("买菜")
	t3 = Task("学Python")
	print(t1)
	print(t2)
	print(t3)
	t1.mark_done()
	t3.mark_done()
	print("\n标记完成后：")
	print(t1)
	print(t2)
	print(t3)
	print(f"\n任务名：{t1.name}")
	print(f"\n是否完成：{t1.done}")
