from pathlib import Path
from datetime import date,datetime,timedelta
from collections import Counter,defaultdict

#目标目录
TARGET = Path.home()/"ai-learning-log"/"week03"

#今天和昨天
today = date.today()
yesterday = today - timedelta(days = 1)

#收集所有文件
files = []
for p in TARGET.iterdir():
	if p.is_file():
		files.append(p)

#TODO 1：用Counter统计扩展名
ext_counter = Counter()
for p in files:
	ext = p.suffix or "无扩展名"
	ext_counter[ext] +=1 

#TODO2:用defaultdict(list)按修改日期分组
by_date = defaultdict(list)
for p in files:
	mtime = datetime.fromtimestamp(p.stat().st_mtime).date()
	if mtime == today:
		by_date["今天"].append(p.name)
	elif mtime == yesterday:
		by_date["昨天"].append(p.name)
	else:
		by_date["更早"].append(p.name)

#TODO3：打印结果
print("=====文件统计=====")
print(f"总文件数：{len(files)}")
print

print("按扩展名统计：")
for ext,count in ext_counter.most_common():
	print(f"{ext:10s}:{count}")
print()

print("按修改日期分组：")
for label in ["今天","昨天","更早"]:
	names = by_date[label]
	if names:
		print(f"{label}:{','.join(names)}")
