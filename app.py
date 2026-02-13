import streamlit as st
from groq import Groq

st.set_page_config(page_title="Salary Negotiation ChatBot", page_icon="👨🏻‍💻")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("👨🏻‍💻 Salary Negotiation ChatBot")
st.markdown("Ask me anything about salary negotiation!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask your question..."):

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a professional salary negotiation coach for tech placements in India."},
                *st.session_state.messages
            ],
            model="llama3-8b-8192",
        )

        reply = chat_completion.choices[0].message.content
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
