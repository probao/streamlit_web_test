import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

os.environ["OPENAI_API_BASE"] = "https://api.gpts.vin/v1"
# Initialize the ChatOpenAI object
chat = None

if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""
elif st.session_state["OPENAI_API_KEY"] != "":
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"])

if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ""

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ""

st.set_page_config(page_title="Welcome to ASL", layout="wide")

st.title("🤠 Welcome to ASL")

with st.container():
    st.header("Open AI Settings")
    st.markdown(f"""
        | OpenAI API Key |
        | -------------- |
        | {st.session_state["OPENAI_API_KEY"]}|
                """)

with st.container():
    st.header("Pinecone Settings")
    st.markdown(f"""
        | Pinecone API Key | Environment |
        | ---------------- | ----------- |
        |{st.session_state["PINECONE_API_KEY"]} | {st.session_state["PINECONE_ENVIRONMENT"]}
                """)

if chat:
    with st.container():
        st.header("CHat with GPT")
        prompt = st.text_input("Prompt", value="", max_chars=None, key=None, type="default")
        asked = st.button("Ask")
        if asked:
            ai_message = chat([HumanMessage(content = prompt)])
            st.write(ai_message.content)

            