import streamlit as st

def set_green_theme():
    st.markdown("""
        <style>
        body, .stApp {
            background-color: #e6ffe6;
        }
        .stButton>button {
            background-color: #228B22;
            color: white;
            border-radius: 8px;
        }
        label, .stRadio label, .stRadio>div>label, .stRadio div[role="radio"], .stSelectbox>div>label, .stNumberInput>div>label, .stSlider>div>label {
            color: #006400 !important;
            font-weight: 600;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #228B22;
        }
        </style>
    """, unsafe_allow_html=True)
