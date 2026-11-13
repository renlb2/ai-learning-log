from pypdf import PdfReader
import docx
import pandas as pd
import pdfplumber
from pathlib import Path
import re


# 0. 准备测试环境
base_dir = Path("week07")
docx_path = base_dir / "test.docx"
xlsx_path = base_dir / "test.xlsx"

# 生成一个测试 Word 文件
d = docx.Document()
d.add_heading('公司保密制度', 0)
d.add_paragraph('本文件属于绝密级别。')
d.add_paragraph('严禁将本文件的内容发送给外部人员。')
d.save(docx_path)

# 生成一个测试 Excel 文件
df = pd.DataFrame({
    "部门": ["研发部", "市场部", "人事部"],
    "年假天数": [15, 10, 12],
    "负责人": ["张三", "李四", "王五"]
})
df.to_excel(xlsx_path, index=False)

print("测试文件已生成！\n" + "="*30)

# ================= 1. 解析 PDF =================
# 注意：这里假设你有一个 sample.pdf。如果没有，可以用 word 导出，或者跳过看后面的逻辑
try:
    pdf_path = base_dir / "123个亏钱案例（第一版）.pdf" 
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text(layout=True) 
    
        # 1. 看看提取到的总字符数（应该很多）
        print(f"【总共提取字符数】: {len(text)}")
    
        # 2. 把前面的空格和换行全去掉，再打印前100字
        stripped_text = text.strip()
        print("【去掉空白后的前100字】:\n")
        print(stripped_text[:100]) 

    # 假设 text 是你刚才通过 pdfplumber 提取出来的 5311 个字符
    # 1. 把多余的空格和连续换行干掉
    cleaned = re.sub(r'[ \t]+', ' ', text) 
    cleaned = re.sub(r'\n+', '\n', cleaned)

    # 2. 干掉顶部的引流广告和底部的二维码提示
    # 用正则匹配包含“公众号”、“老庄个人微信”的整行并删除
    cleaned = re.sub(r'.*公众号.*\n', '', cleaned)
    cleaned = re.sub(r'.*老庄个人微信.*\n', '', cleaned)

    print("【清洗后的前200字】:\n")
    print(cleaned.strip()[:200])


except FileNotFoundError:
    print("【PDF】跳过：当前目录没有 sample.pdf\n")

# ================= 2. 解析 Word =================
doc = docx.Document(docx_path)
# 提取所有段落
docx_text = "\n".join([para.text for para in doc.paragraphs])
print(f"【Word 提取结果】:\n{docx_text}\n")

# ================= 3. 解析 Excel =================
# Excel 不像文本文档，需要转成 Markdown 表格或自然语言
excel_df = pd.read_excel(xlsx_path)
# 方法 A：转成字典列表（适合结构化处理）
excel_records = excel_df.to_dict(orient="records")
# 方法 B：转成 Markdown 格式（适合直接喂给大模型）
excel_md = excel_df.to_markdown(index=False)

print(f"【Excel 提取结果 - 字典】:\n{excel_records}\n")
print(f"【Excel 提取结果 - Markdown表格】:\n{excel_md}\n")
