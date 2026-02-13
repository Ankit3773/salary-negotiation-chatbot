import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("Salary Negotiation ChatBot")

user_input = st.text_input("Ask your negotiation question:")

if user_input:
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a professional salary negotiation coach for tech placements in India."},
            {"role": "user", "content": user_input}
        ],
        model="llama3-8b-8192",
    )

    st.write(chat_completion.choices[0].message.content)

# Page config
st.set_page_config(page_title="Salary Negotiation ChatBot", page_icon="👨🏻‍💻")

# 👇 Custom Header
st.markdown(
    """
    <div style='text-align: center; padding: 10px; border-bottom: 2px solid #ddd;'>
        <h3>ANKIT KUMAR - 12319407</h3>
       
    </div>
    """,
    unsafe_allow_html=True
)

# App title and intro
st.title("👨🏻‍💻 Salary Negotiation ChatBot")
st.markdown("Ask me anything about Salary!")
st.success("👋 !")

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
