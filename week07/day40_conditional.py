from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class MyState(TypedDict):
    text: str
    is_english: bool

def check_language(state: MyState):
    # 简单的判断：如果有英文字母就是英文
    has_eng = any(c.isalpha() and c.isascii() for c in state["text"])
    print(f"--- 判断语言：{'英文' if has_eng else '中文'} ---")
    return {"is_english": has_eng}

def handle_english(state: MyState):
    print("--- 处理英文 ---")
    return {"text": state["text"].upper()}

def handle_chinese(state: MyState):
    print("--- 处理中文 ---")
    return {"text": state["text"] + "（已处理）"}

# 路由函数：决定下一步去哪
def route_language(state: MyState):
    if state["is_english"]:
        return "english_node"
    else:
        return "chinese_node"

builder = StateGraph(MyState)
builder.add_node("check", check_language)
builder.add_node("english_node", handle_english)
builder.add_node("chinese_node", handle_chinese)

builder.add_edge(START, "check")

# 重点：添加条件边！根据 route_language 的返回值决定走哪条线
builder.add_conditional_edges("check", route_language)
# 注：目标节点的末尾都连到 END
builder.add_edge("english_node", END)
builder.add_edge("chinese_node", END)

graph = builder.compile()

# 测试
print("== 测试英文 ==")
graph.invoke({"text": "hello graph", "is_english": False})

print("\n== 测试中文 ==")
graph.invoke({"text": "你好，大模型", "is_english": False})
