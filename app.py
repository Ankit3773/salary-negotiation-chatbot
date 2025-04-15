import streamlit as st
import openai
import os

# Load your OpenAI API key (store securely using secrets or environment variables)
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Salary Negotiation Chatbot", page_icon="💬")

st.title("💼 Salary Negotiation Chatbot")
st.markdown("Ask me anything about negotiating your salary!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are an expert salary negotiation coach. Help users practice and prepare for real conversations with employers."}
    ]

# Display chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
prompt = st.chat_input("Ask me about salary negotiation...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call OpenAI API
    with st.chat_message("assistant"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.markdown(reply)

    # Add assistant response
    st.session_state.messages.append({"role": "assistant", "content": reply})
