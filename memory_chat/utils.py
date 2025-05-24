import streamlit as st

def initialize_session():
    if "input_text" not in st.session_state:
        st.session_state.input_text = ""
    if "persona" not in st.session_state:
        st.session_state.persona = "default"
    if "theme" not in st.session_state:
        st.session_state.theme = "light"