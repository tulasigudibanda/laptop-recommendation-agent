import streamlit as st
from agent import ask_agent
import requests

st.set_page_config(
    page_title="Laptop Recommendation Agent",
    page_icon="💻"
)

# -----------------------------
# Session State
# -----------------------------
# if "brand" not in st.session_state:
#     st.session_state.brand = None

# if "budget" not in st.session_state:
#     st.session_state.budget = None

# if "ram" not in st.session_state:
#     st.session_state.ram = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# UI
# -----------------------------
st.title("💻 Laptop Recommendation Agent")

# Show previous conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask me about laptops")

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    # Call agent
    with st.spinner("Thinking..."):
        # answer = ask_agent(
        #     st.session_state.messages,
        #     # brand=st.session_state.brand
        # )

        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={
                "messages": st.session_state.messages
            }
        )

        answer = response.json()["answer"]

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(answer)
