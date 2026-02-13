import streamlit as st
from groq import Groq

# Page config MUST be first
st.set_page_config(page_title="Salary Negotiation ChatBot", page_icon="👨🏻‍💻")

# Initialize Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Custom Header
st.markdown(
    """
    <div style='text-align: center; padding: 10px; border-bottom: 2px solid #ddd;'>
        <h3>ANKIT KUMAR - 12319407</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("👨🏻‍💻 Salary Negotiation ChatBot")
st.markdown("Ask me anything about Salary Negotiation!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask me about salary negotiation..."):

    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Groq response
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
