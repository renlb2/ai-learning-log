# Day 37 - 多格式文档解析与文本清洗

## 核心知识点

### 1. 多格式文档解析工具
- **PDF (`pypdf` / `pdfplumber`)**：
  - PDF 底层是坐标绘制，没有段落概念。`pypdf` 提取容易出现顺序错乱。
  - `pdfplumber` 的版面分析更强，`extract_text(layout=True)` 保留物理排版（但会带大量空格），`strip()` 清洗后效果更好。
- **Word (`python-docx`)**：按段落（`paragraphs`）提取，文字质量通常最高，极少有乱码。
- **Excel (`pandas` + `openpyxl`)**：不要直接转字符串。用 `to_dict(orient="records")` 转字典，或用 `to_markdown()` 转 Markdown 表格（需安装 `tabulate` 库），大模型对 Markdown 表格的理解极强。

### 2. 文本清洗（Data Cleaning）四步曲
工业级 RAG 中，**“垃圾进，垃圾出”**。提取出的文本必须经过正则清洗：
1. 去除多余空格：`re.sub(r'[ \t]+', ' ', text)`
2. 去除连续换行：`re.sub(r'\n+', '\n', text)`
3. 去除不可见字符：`re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)`
4. **去除业务噪音**：用正则过滤页眉页脚、公众号引流、页码等（如 `re.sub(r'.*公众号.*\n', '', text)`）。

## 产出
- `week07/day37_parsers.py`（PDF/Word/Excel 解析 + 正则清洗）
- `week07/day37_final_rag.py`（完整的 Word 解析 -> 切片 -> 入库 -> 检索问答）
- `week07/test.docx` / `week07/test.xlsx`（测试数据）

## 踩坑与反思
- **依赖缺失**：`pandas.to_markdown()` 会报错，需要 `pip install tabulate`。
- **PDF 顺序错乱**：真实世界的 PDF 经常掺杂二维码、水印、双栏排版，导致提取顺序混乱。
- **清理噪音是必须的**：如果不把“公众号引流”正则干掉，RAG 检索时会把广告当成知识喂给大模型。

## 明天（Day 38）
扔掉手工作坊，拥抱 **LangChain**。用 10 行代码重构这三天的所有活。
