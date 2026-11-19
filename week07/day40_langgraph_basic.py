from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 1. 定义状态（数据袋子）
class MyState(TypedDict):
    text: str
    count: int

# 2. 定义节点（干活的函数）
def node_process_text(state: MyState):
    print("--- 正在执行：处理文本节点 ---")
    # 把所有的字母转成大写
    new_text = state["text"].upper()
    # 返回更新后的状态
    return {"text": new_text}

def node_count_words(state: MyState):
    print("--- 正在执行：统计单词节点 ---")
    # 统计单词数量
    words = state["text"].split()
    return {"count": len(words)}

# 3. 组装流程图
builder = StateGraph(MyState)

# 添加节点
builder.add_node("process", node_process_text)
builder.add_node("count", node_count_words)

# 添加边（定义执行顺序）
builder.add_edge(START, "process") # 起点 -> process
builder.add_edge("process", "count") # process -> count
builder.add_edge("count", END)     # count -> 终点

# 编译成可运行的图
graph = builder.compile()

# 4. 运行
print("开始运行工作流...")
initial_state = {"text": "hello langgraph this is awesome", "count": 0}
result = graph.invoke(initial_state)

print("\n执行结果：", result)
