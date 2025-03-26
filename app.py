# Home.py
import streamlit as st

st.set_page_config(
    page_title="MOOC Solutions",
    page_icon="solar.jpg", 
    layout="wide",  # Try wide layout to ensure sidebar is visible
    initial_sidebar_state="expanded"  # Force sidebar to be open
)

# Add a title to the sidebar
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

# No need to manually create page navigation - Streamlit does this automatically
# with the multipage app structure

# Your page content
st.title("MOOC Solutions")
st.write("Welcome to MOOC Solutions! Use the sidebar to navigate between courses and mock tests.")

# Add image and QR code to sidebar
st.sidebar.markdown('<br>' * 4, unsafe_allow_html=True)
st.sidebar.image("qr.jpeg", width=300)
st.sidebar.markdown('<div style="text-align: center;">Buy me a coffee ☕</div>', unsafe_allow_html=True)