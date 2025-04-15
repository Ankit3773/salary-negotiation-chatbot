import streamlit as st
import google.generativeai as genai

# Load your API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Set up model
model = genai.GenerativeModel("gemini-pro")

# Streamlit UI
st.set_page_config(page_title="Salary Negotiation Chatbot", page_icon="💼")
st.title("💼 Salary Negotiation Chatbot")
st.markdown("Ask me anything about negotiating your salary!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask me about salary negotiation...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response = model.generate_content(user_input)
        reply = response.text
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
