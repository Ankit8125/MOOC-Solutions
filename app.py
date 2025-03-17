import streamlit as st

st.set_page_config(
    page_title="MOOC Solutions",
    page_icon="solar.jpg", 
    layout="centered",
    initial_sidebar_state="auto"
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
    st.title("MOOC Solutions")

    # Sidebar with options
    selected_option = st.sidebar.radio(
        "Select Course",
        ["Conservation Economics", "Psychology of Learning"],
        index=0  # Default to "Conservation Economics"
    )

    st.header(selected_option)
    content_dict = {
        "Conservation Economics": {
            "Week 1": ["A", "B", "D", "B", "C", "A", "C", "C", "B", "B"],
            "Week 2": ["C", "C", "A", "C", "A", "A", "C", "B", "C", "B"],
            "Week 3": ["B", "D", "B", "B", "D", "B", "A", "A", "C", "C"],
            "Week 4": ["C", "D", "A", "C", "B", "D", "C", "C", "A", "A"],
            "Week 5": ["A", "B", "B", "C", "B", "C", "D", "A", "B", "B"],
            "Week 6": ["A", "A", "B", "D", "A", "B", "C", "A", "A", "A"],
            "Week 7": ["C", "A", "A", "B", "C", "D", "B", "A", "A", "B"],
            "Week 8": ["C", "B", "A", "A", "B", "C", "D", "B", "C", "B"],
            "Week 9": ["D", "A", "C", "A", "D", "A", "A", "A", "B", "A"],
        },
        "Psychology of Learning": {
            "Week 1": ["D", "D", "A", "A", "C", "A", "A", "D", "D", "C"],
            "Week 2": ["B", "C", "C", "C", "A", "A", "D", "B", "A", "A"],
            "Week 3": ["D", "C", "A", "C", "C", "A", "B", "A", "D", "C"],
            "Week 4": ["D", "C", "D", "C", "A", "A", "D", "B", "A", "D"],
            "Week 5": ["C", "B", "B", "A", "A", "A", "D", "B", "A", "D"],
            "Week 6": ["C", "C", "A", "D", "A", "A", "D", "D", "C", "B"],
            "Week 7": ["C", "D", "D", "D", "A", "A", "D", "E", "A", "B"],
            "Week 8": ["C", "B", "B", "C", "A", "A", "D", "D", "A", "B"],
            "Week 9": ["C", "B", "D", "D", "D", "C", "C", "D", "A", "A"],
            "Week 10": ["C", "B", "D", "D", "A", "D", "C", "D", "A", "D"],
            "Week 11": ["C", "D", "A", "D", "B", "C", "D", "A", "A", "B"],
            "Week 12": ["C", "D", "A", "B", "C", "B", "D", "A", "A", "B"],
        }
    }

    weeks = list(content_dict[selected_option].keys())
    selected_week = st.selectbox("Select a Week", weeks, key="week_selectbox")

    if selected_week:
        content_items = content_dict[selected_option][selected_week]
        content_display = "\n".join([f"{i+1}) {item}" for i, item in enumerate(content_items)])
        st.write(f"Answers for {selected_week}:")
        st.write(content_display)
    create_footer()

if __name__ == "__main__":
    main()
