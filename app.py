import streamlit as st

from agent import ask_agent

st.set_page_config(
    page_title="Laptop Recommendation Agent",
    page_icon="💻"
)

st.title("💻 Laptop Recommendation Agent")

question = st.text_input(
    "Ask me about laptops"
)

if st.button("Recommend"):

    with st.spinner("Thinking..."):

        answer = ask_agent(question)

    st.success(answer)