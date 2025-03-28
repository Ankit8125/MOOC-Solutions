import streamlit as st

st.set_page_config(
    page_title="Conservation Economics",
    page_icon="solar.jpg", 
    layout="centered"
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

def create_footer():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f8f9fa;
            color: black;
            text-align: center;
            padding: 10px 0;
        }
        .footer a {
            color: #007bff;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        </style>
        <div class="footer">
            Created by <a href="https://www.linkedin.com/in/ankitverma2405/" target="_blank">Ankit Verma (aka Solar System)</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

def main():
    st.title("Conservation Economics")
    
    content_dict = {
        "Week 1": ["A", "B", "D", "B", "C", "A", "C", "C", "B", "B"],
        "Week 2": ["C", "C", "A", "C", "A", "A", "C", "B", "C", "B"],
        "Week 3": ["B", "D", "B", "B", "D", "B", "A", "A", "C", "C"],
        "Week 4": ["C", "D", "A", "C", "B", "D", "C", "C", "A", "A"],
        "Week 5": ["A", "B", "B", "C", "B", "C", "D", "A", "B", "B"],
        "Week 6": ["A", "A", "B", "D", "A", "B", "C", "A", "A", "A"],
        "Week 7": ["C", "A", "A", "B", "C", "D", "B", "A", "A", "B"],
        "Week 8": ["C", "A", "A", "A", "B", "C", "D", "B", "C", "B"],
        "Week 9": ["D", "A", "C", "A", "D", "A", "A", "A", "B", "A"],
        "Week 10": ["B", "C", "C", "B", "A", "B", "B", "A", "B", "A"],
        "Week 11": ["B", "C", "B", "A", "B", "B", "C", "C", "A", "D"],
        "Week 12": ["Aaram se wait karna brooo! Jab aayega toh daal dunga :P"],
    }

    weeks = list(content_dict.keys())
    selected_week = st.selectbox("Select a Week", weeks, key="week_selectbox")

    if selected_week:
        content_items = content_dict[selected_week]
        content_display = "\n".join([f"{i+1}) {item}" for i, item in enumerate(content_items)])
        st.write(f"Answers for {selected_week}:")
        st.write(content_display)
        
    st.sidebar.markdown('<br>' * 3, unsafe_allow_html=True)
    st.sidebar.image("qr.jpeg", width=300)
    st.sidebar.markdown('<div style="text-align: center;">Buy me a coffee ☕ :)</div>', unsafe_allow_html=True)
    
    create_footer()

if __name__ == "__main__":
    main()
