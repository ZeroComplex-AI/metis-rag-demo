import os
import uuid
import streamlit as st
from services import bedrock_agent
from dotenv import load_dotenv

load_dotenv()


def init_state():
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.messages = []
    st.session_state.citations = []


# STREAMLIT UI
st.set_page_config(page_title="Metis RAG", layout="centered")
st.title("Metis Conversational AI")
st.write("Enter your query below:")

if not st.session_state.items():
    init_state()

with st.sidebar:
    st.title("Knowledge Base Overview")
    st.caption(
        f"Metis RAG is trained on a knowledge base provisioned in Amazon Bedrock."
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

if promptText := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": promptText})
    with st.chat_message("user"):
        st.write(promptText)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("...")
        response = bedrock_agent.invoke_agent(promptText, st.session_state.session_id)
        output_text = response["output_text"]

        placeholder.markdown(output_text, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": output_text})
