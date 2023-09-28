from backend.core import run_llm
import time
import streamlit as st
from streamlit_chat import message
from typing import Set

st.header("LangChain - A Network Example")
prompt = st.text_input("Prompt", placeholder="Enter your request...")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []
if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []


def create_sources_string(source_urls: Set[str]) -> str:
    ...


if prompt:
    with st.spinner("Retrieving response..."):
        generated_response = run_llm(query=prompt)
        formatted_response = f"{generated_response['result']} \n\n "
        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)

if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(user_query, is_user=True)
        message(generated_response)
