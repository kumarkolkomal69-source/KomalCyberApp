import streamlit as st

# ऐप की सेटिंग
st.set_page_config(page_title="Cyber-Core AI", layout="wide")

# डिज़ाइन (CSS)
st.markdown("""
    <style>
    html, body, [class*="css"] { background-color: #0e0e0e; color: white; }
    .stButton>button { border-radius: 20px; background: #4285F4; color: white; border: none; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# लॉगिन सिस्टम
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<h2 style='text-align: center;'>🧬 Cyber-Core Portal</h2>", unsafe_allow_html=True)
    user = st.text_input("यूजर आईडी (ID):")
    pin = st.text_input("पासवर्ड (PIN):", type="password")
    if st.button("Unlock System"):
        if user.lower() == "komal" and pin == "1234":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("गलत आईडी या पासवर्ड!")
else:
    # ऐप खुलने के बाद का हिस्सा
    st.title("🚀 Cyber-Core Neural Engine")
    st.write("स्वागत है कोमल! लैब सुरक्षित है और सिस्टम ऑनलाइन है।")
    
    msg = st.chat_input("आदेश दें...")
    if msg:
        st.chat_message("user").write(msg)
        st.chat_message("assistant").write(f"नमस्ते कोमल, मैंने आपके आदेश पर काम शुरू कर दिया है।")
