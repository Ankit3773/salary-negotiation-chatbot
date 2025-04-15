import streamlit as st
import google.generativeai as genai

# Set Streamlit page config
st.set_page_config(
    page_title="💼 Salary Negotiation Chatbot",
    page_icon="💼",
    layout="centered"
)

# Custom CSS for cleaner look
st.markdown("""
    <style>
    .message {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .user {
        background-color: #1f2937;
        color: white;
    }
    .bot {
        background-color: #2d3748;
        color: #ffebcd;
    }
    </style>
""", unsafe_allow_html=True)

# Set your Gemini API key from Streamlit secrets
os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini 2.0 model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

# App title
st.title("💼 Salary Negotiation Chatbot")
st.subheader("💬 Ask me anything about negotiating your salary!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    with st.container():
        if msg["role"] == "user":
            st.markdown(f'<div class="message user">👤 {msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="message bot">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

# Chat input
prompt = st.chat_input("Ask me about salary negotiation...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Gemini response
    response = model.generate_content(prompt)
    bot_reply = response.text

    st.session_state.messages.append({"role": "bot", "content": bot_reply})
    st.experimental_rerun()
