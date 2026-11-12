from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. 模拟一段很长的公司文档（或者你可以用 open() 读取真实的 txt/pdf 文件）
sample_text = """
公司年度总结与规章制度。员工每年享有 15 天的带薪年假，需提前 3 天在 OA 系统申请。
请假流程：先找直属领导审批，再抄送给 HR。如果遇到法定节假日，则顺延。
关于报销：打车费每月限额 500 元，凭发票报销。超过 500 元需部门总监审批。差旅住宿标准：一线城市 600 元/晚。
食堂规定：中午 12:00 开饭，员工免费就餐，禁止打包。晚饭时间为 18:00，仅限加班人员。
"""

# 2. 初始化切片器
# chunk_size=50：每块大约 50 个字
# chunk_overlap=10：相邻两块之间有 10 个字的重叠（防止上下文被一刀切断）
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10,
    length_function=len,
    keep_separator="end",
    separators=["\n\n", "\n", "。", "，", " ", ""] # 优先按段落切，其次按句号，再按逗号
)

# 3. 执行切片
chunks = text_splitter.split_text(sample_text)

print(f"原文总字数: {len(sample_text)}")
print(f"切分后总共变成了 {len(chunks)} 块：\n")

for i, chunk in enumerate(chunks):
    print(f"--- 第 {i+1} 块 (长度 {len(chunk)}) ---")
    print(chunk)
    print()
