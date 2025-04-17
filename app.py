import streamlit as st
import google.generativeai as genai
import os


os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")


st.set_page_config(page_title="Salary Negotiation Chatbot", page_icon="💼")

st.markdown(
    """
    <div style='text-align: center; padding: 10px; border-bottom: 2px solid #ddd;'>
        <h3>ANKIT KUMAR - 12319407</h3>
        <h3>AAYUSH KUMAR - 12319413</h3>
    </div>
    """,
    unsafe_allow_html=True
)


st.title("💼 Salary Negotiation Chatbot")
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

    with st.chat_message("assistant"):
       # Keywords related to salary negotiation
keywords = ["salary", "negotiation", "offer", "counter", "pay", "package", "hike", "compensation"]

# Check if user input is relevant
if any(keyword in user_input.lower() for keyword in keywords):
    response = model.generate_content(user_input)
    reply = response.text
else:
    reply = "❌ Sorry, I can only help with salary negotiation-related questions."

st.markdown(reply)
st.session_state.messages.append({"role": "assistant", "content": reply})
