import streamlit as st
from groq import Groq

# --- CONFIG ---
st.set_page_config(page_title="Uttam AI Chatbot 🤖", layout="centered")

# --- TITLE ---
st.title("🤖 Uttam's AI Chatbot")
st.write("Powered by Free AI (Groq + Llama 3)")

# --- API CLIENT ---
client = Groq(api_key="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")

# --- SESSION MEMORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- DISPLAY CHAT HISTORY ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- USER INPUT ---
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    # Store AI reply
    st.session_state.messages.append({"role": "assistant", "content": reply})

    # Show AI reply
    with st.chat_message("assistant"):
        st.markdown(reply)
