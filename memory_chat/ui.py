import streamlit as st
from memory_chat.chat_engine import get_response
from memory_chat.memory_manager import memory_store
from memory_chat.utils import initialize_session
import base64


def launch_ui():
    st.set_page_config("Memory Chatbot", layout="wide")
    initialize_session()

    with st.sidebar:
        st.header("🧠 Tools")

        with st.expander("🎭 Persona", expanded=True):
            st.session_state.persona = st.selectbox("Choose Persona", ["default", "therapist", "coder"], key="persona_select")

        with st.expander("🌓 Theme", expanded=False):
            st.session_state.theme = st.radio("Choose Theme", ["light", "dark"], key="theme_select")

        with st.expander("🔍 Search Memory", expanded=False):
            keyword = st.text_input("Keyword", key="search_keyword")
            if keyword:
                search_results = memory_store.search_memory(keyword)
                st.text_area("Search Results", "\n".join([f"{m['role']}: {m['content']}" for m in search_results]), height=150)

        with st.expander("🗂 Export Memory", expanded=False):
            export_format = st.selectbox("Format", ["text", "markdown", "json"], key="export_format")
            export_data = memory_store.export_memory(export_format)
            b64 = base64.b64encode(export_data.encode()).decode()
            st.download_button("Download Memory", data=export_data, file_name=f"chat_memory.{export_format}", mime="text/plain")

        with st.expander("🧹 Clear & Reset", expanded=False):
            if st.button("Clear Memory"):
                memory_store.clear()
                st.experimental_rerun()

        with st.expander("📚 Long-Term Memory", expanded=False):
            if st.button("View Long-Term Memory"):
                long_term_memory = memory_store.get_long_term_memory()
                st.text_area("Long-Term Memory", long_term_memory, height=250)

    st.title("🧠 Memory Enhanced Chatbot")
    chat_container = st.container()

    with chat_container:
        for msg in memory_store.get_conversation():
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        prompt = st.chat_input("Say something...")
        if prompt:
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    reply = get_response(prompt, st.session_state.persona)
                    st.markdown(reply)
                with st.expander("🤖 AI Thought Process"):
                    st.write("This message was generated using memory context and persona configuration.")
