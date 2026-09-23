from pathlib import Path
import shutil
import sys

#=====配置=====
DRY_RUN = False

TARGET = Path.home()/"ai-learning-log"/"week04"/"test_organize"  #指定目录

RULES = {
	".py":"python",
	".md":"markdown",
	".json":"json",
}								#字典，扩展名：分类目录的名字

#=====工具函数：防止覆盖"=====
def safe_dest(dst:Path)->Path:
	if not dst.exists():
		return dst
	stem,suffix = dst.stem,dst.suffix			#目标路径正常的话，获取文件名，扩展名
	i = 1
	while True:						#存在重名文件的，把文件文件命名成”文件名_数字”的形式
		new = dst.with_name(f"{stem}_{i}{suffix}")
		if not new.exists():
			return new
		i += 1

#=====主逻辑=====
def organize():
	if not TARGET.exists():
		print(f"目录不存在：{TARGET}")
		return

	moved = 0
	for p in TARGET.iterdir():
		if not p.is_file():				#跳过目录
			continue

		ext = p.suffix.lower()				#遍历源文件目录下的文件，获取扩展名，转成小写
		sub = RULES.get(ext,"others")			#根据扩展名，选择目标目录名，不在字典里的，统一选择”others”
		dest_dir = TARGET/sub				#拼接成完整的目录名
		dest = safe_dest(dest_dir/p.name)		#生成文件名

		if DRY_RUN:
			print(f"[DRY_RUN]{p.name}->{sub}/{dest.name}")
		else:
			dest_dir.mkdir(exist_ok=True)
			shutil.move(str(p),str(dest))
			print(f"[move]{p.name}->{sub}/{dest.name}")
			moved +=1

	if DRY_RUN:
		print("\n以上为预演，未移动任何文件。确认后把DRY_RUN改为False再跑。")
	else:
		print(f"\n完成，共移动{moved}个文件。")

if __name__ == "__main__":
	organize()
