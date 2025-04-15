import streamlit as st
import openai
import os

# Load your OpenAI API key
openai.api_key = st.secrets["6d675b9202cf46f2a06b27244890661d"]

st.set_page_config(page_title="Salary Negotiation Chatbot", page_icon="💬")

st.title("💼 Salary Negotiation Chatbot")
st.markdown("Ask me anything about negotiating your salary!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI salary negotiation coach. Give smart, practical advice and example phrases."}
    ]

# Show chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask your question here...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
