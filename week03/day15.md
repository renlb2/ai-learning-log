# Day 15 - pathlib 重写通讯录

## 今日目标
用 pathlib 替代 os.path，重构 save/load，并增加自动备份功能。

## 核心知识点
- Path 用 / 拼路径，替代 os.path.join
- Path.read_text / write_text 替代 open()
- Path.mkdir(parents=True, exist_ok=True) 建多层目录
- __file__ + resolve().parent 定位脚本所在目录
- shutil.copy 实现覆盖前备份

## 产出
- week03/data/contacts.json（2 条）
- week03/data/backup/contacts_backup.json（1 条）
- 代码已用 pathlib 重构

## 验证结果
- 第二次启动能 load 出小明 ✅
- 覆盖保存后 backup 里保留上次数据 ✅
- 目录自动创建，无需手动 mkdir ✅

## 明天（Day 16）
datetime / collections + 文件整理脚本启动
