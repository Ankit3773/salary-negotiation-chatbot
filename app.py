import streamlit as st
import google.generativeai as genai
import os

# Set your Gemini API key from Streamlit secrets
os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini 2.0 model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

# Page config
st.set_page_config(page_title="Salary Negotiation Chatbot", page_icon="💼")

# 👇 Custom Header
st.markdown(
    """
    <div style='text-align: center; padding: 10px; border-bottom: 2px solid #ddd;'>
        <h3>ANKIT KUMAR - 12319407</h3>
        <h3>AAYUSH KUMAR - 12319413</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# App title and intro
st.title("💼 Salary Negotiation Chatbot")
st.markdown("Ask me anything about negotiating your salary!")
st.success("👋 Welcome! Ask me anything about salary negotiations. Let's boost your paycheck!")

# Store chat history in session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
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
