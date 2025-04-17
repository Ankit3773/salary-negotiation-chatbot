import streamlit as st
import google.generativeai as genai
import os

os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

st.set_page_config(page_title="Salary Negotiation Chatbot", page_icon="💼")
st.title("💼 Salary Negotiation Chatbot")
st.markdown("##### 👨‍🎓 Ankit Kumar (12319407) | Aayush Kumar (12319413)")
st.markdown("Ask me anything about negotiating your salary!")
st.success("👋 Welcome! Ask me anything about salary negotiations. Let's boost your paycheck!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask me about salary negotiation...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    keywords = ["salary", "negotiation", "offer", "counter", "pay", "package", "hike", "compensation", "ctc", "appraisal"]

    if any(keyword in user_input.lower() for keyword in keywords):
        with st.chat_message("assistant"):
            response = model.generate_content(user_input)
            reply = response.text
            st.markdown(reply)
    else:
        reply = "❌ Sorry, I can only help with salary negotiation-related questions."
        with st.chat_message("assistant"):
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
