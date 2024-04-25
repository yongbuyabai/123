import os
import openai
# 设置你的OpenAI API密钥
api_key = os.environ.get("OPENAI_API_KEY")
# 创建OpenAI客户端
client = openai.ChatCompletion.create(
    api_key=api_key
)
# 发送消息给GPT-3进行对话
response = client.create(
    messages=[
        {
            "role": "user",
            "con  te  nt": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)
# 输出GPT-3的响应
print(response)
