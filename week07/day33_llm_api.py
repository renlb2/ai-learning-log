from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ZHIPU_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)

response = client.chat.completions.create(
    model="glm-4-flash",  # 免费模型
    temperature=0,
    messages=[
        {"role": "system", "content": "你是一个严谨的数学老师，只输出最终的阿拉伯数字答案，不要包含任何其他汉字或标点。"},
        {"role": "user", "content": "一根绳子对折 3 次后，从中间剪断，一共变成了几段？"}
    ]
)

print(response.choices[0].message.content)
