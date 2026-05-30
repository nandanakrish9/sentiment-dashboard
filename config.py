

import streamlit as st

try:
    API_KEY = st.secrets["dace758b66514bcfb07d8b876f96afa1"]
except:
    from dotenv import load_dotenv
    import os
    load_dotenv()
    API_KEY = os.getenv("dace758b66514bcfb07d8b876f96afa1")