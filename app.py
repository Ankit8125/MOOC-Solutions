# Home.py
import streamlit as st

st.set_page_config(
    page_title="MOOC Solutions",
    page_icon="solar.jpg", 
    layout="wide",  # Try wide layout to ensure sidebar is visible
    initial_sidebar_state="expanded"  # Force sidebar to be open
)

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] li:first-child {
            display: none;
        }
    
        /* Capitalize each entry in the sidebar */
        [data-testid="stSidebarNav"] span {
            text-transform: capitalize;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

st.title("MOOC Solutions")
st.write("Welcome to MOOC Solutions! Use the sidebar to navigate between courses and mock tests.")

st.sidebar.markdown('<br>' * 4, unsafe_allow_html=True)
st.sidebar.image("qr.jpeg", width=300)
st.sidebar.markdown('<div style="text-align: center;">Buy me a coffee ☕ :)</div>', unsafe_allow_html=True)