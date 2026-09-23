# Day 16 - datetime + collections + 文件统计

## 核心知识点
- datetime.fromtimestamp() 把 st_mtime 时间戳转成日期
- date.today() / timedelta(days=1) 算今天和昨天
- Counter 统计扩展名数量，most_common() 排序
- defaultdict(list) 按日期分组，key 不存在时自动建空列表
- Path.iterdir() + is_file() 遍历一层文件，不递归

## 产出
- week04/day16_file_stats.py
- 统计结果：6 个文件，.py 4 / .md 1 / .json 1

## 踩坑
- 中文引号导致 SyntaxError：字符串引号必须用英文 " 或 '

## 明天（Day 17）
os / shutil 进阶：移动、复制、重命名，开始真正整理文件
