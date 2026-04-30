
import streamlit as st
import base64
from gtts import gTTS
import os
st.set_page_config(page_title="Cyber-Core AI Portal", layout="wide")
st.markdown("""
<style>
.main {background-color: #0e1117; color: #ffffff;}
.stButton>button {width: 100%; border-radius: 10px; background-color: #00ff41; color: black; font-weight: bold;}
</style>
""", unsafe_allow_html=True)
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("⚡ Cyber-Core AI")
    user = st.text_input("यूजर आईडी:")
    pin = st.text_input("पासवर्ड:", type="password")
    if st.button("Unlock System"):
        if user.lower() == "komal" and pin == "1234":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("गलत आईडी या पासवर्ड!")
else:
    st.success("Welcome, Komal ✅")
    st.write("आपका AI पोर्टल सक्रिय है।")
    if st.button("Log Out"):
        st.session_state.auth = False
        st.rerun()
