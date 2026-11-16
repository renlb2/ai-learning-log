# Day 38 - 扔掉手工作坊，拥抱 LangChain

## 核心知识点

### 1. 为什么要用 LangChain？
在 Day 34-37，我们手写了 RAG 全流程（解析 -> 切片 -> 向量化 -> 入库 -> 检索 -> 拼 Prompt -> 调大模型）。
缺点：代码冗长，换个模型或数据库就要大改。
**LangChain** 提供了标准化接口（如 `ChatOpenAI`, `HuggingFaceEmbeddings`, `Chroma`），并用 **LCEL（LangChain 表达式语言）** 把流水线变成了“搭积木”。

### 2. LCEL 流水线（管道符 `|`）
用 `|` 符号像 Linux 管道一样把组件连起来：
```python
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
