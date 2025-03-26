import streamlit as st
from dataclasses import dataclass
from typing import List

st.set_page_config(
    page_title="Mock Test",
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

@dataclass
class Question:
    text: str
    options: List[str]
    correct_answer: str

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
    st.title("Mock Test")
    
    # Define the questions
    MOCK_TEST_QUESTIONS = [
        Question(
            "What is the primary goal of conservation economics?",
            ["Resource exploitation", "Profit maximization", "Sustainable resource management", "Industrial growth"],
            "Sustainable resource management"
        ),
        Question(
            "Which concept refers to the value of an environmental resource simply existing?",
            ["Use value", "Existence value", "Option value", "Bequest value"],
            "Existence value"
        ),
        # Add more questions as needed
    ]
    
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.session_state.score = 0
        st.session_state.test_completed = False
    
    if not st.session_state.test_completed:
        question = MOCK_TEST_QUESTIONS[st.session_state.current_question]
        st.write(f"Question {st.session_state.current_question + 1}/{len(MOCK_TEST_QUESTIONS)}:")
        st.write(question.text)
        
        answer = st.radio("Select your answer:", question.options, key=f"q_{st.session_state.current_question}")
        st.session_state.answers[st.session_state.current_question] = answer
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.session_state.current_question > 0:
                if st.button("Previous"):
                    st.session_state.current_question -= 1
                    st.rerun()
        
        with col2:
            if st.session_state.current_question < len(MOCK_TEST_QUESTIONS) - 1:
                if st.button("Next"):
                    st.session_state.current_question += 1
                    st.rerun()
            else:
                if st.button("Submit Test"):
                    # Calculate score
                    for i, q in enumerate(MOCK_TEST_QUESTIONS):
                        if st.session_state.answers.get(i) == q.correct_answer:
                            st.session_state.score += 1
                    st.session_state.test_completed = True
                    st.rerun()
    
    else:
        st.success(f"Test completed! Your score: {st.session_state.score}/{len(MOCK_TEST_QUESTIONS)}")
        if st.button("Retake Test"):
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.score = 0
            st.session_state.test_completed = False
            st.rerun()
    
    # Add sidebar content
    st.sidebar.markdown('<br>' * 3, unsafe_allow_html=True)
    st.sidebar.image("qr.jpeg", width=300)
    st.sidebar.markdown('<div style="text-align: center;">Buy me a coffee ☕</div>', unsafe_allow_html=True)
    
    create_footer()

if __name__ == "__main__":
    main()