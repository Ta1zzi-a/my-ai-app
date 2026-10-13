import streamlit as st
from openai import OpenAI

st.title("我的 AI 聊天助手")

# ⚠️ 把下面这行换成你自己的 API Key
import os
API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

# 保存聊天历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史消息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 输入框
user_input = st.chat_input("说点什么吧...")

if user_input:
    # 显示用户消息
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 调用 API
    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.write(reply)

    # 保存 AI 回复
    st.session_state.messages.append({"role": "assistant", "content": reply})