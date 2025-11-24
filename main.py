import streamlit as st  
from utils import qa_solver, summarize_text, career_guidance, expand_text

st.set_page_config(  
    page_title="AI Student Study Assistant", 
    page_icon="🎓",  
    layout="wide"  
)
st.markdown("""
<style>
body { background-color: #f5f5f5; color: #1a1a1a; }
h1, h2, h3 { color: #0a3d62; }
.stButton>button { background-color: #0a3d62; color: white; border-radius: 8px; padding: 8px 24px; }
.stTextInput>div>input, .stTextArea>div>textarea { border-radius: 8px; padding: 10px; border: 1px solid #0a3d62; }
</style>
""", unsafe_allow_html=True)
st.title("🎓 AI-Powered Student Study Assistant")
st.write("Professional Chatbot for Q&A, Summarization, and Career Guidance")
tab1, tab2, tab3 = st.tabs(["Q&A Doubt Solver", "Summarizer", "Career Guidance"])
with tab1:
    question = st.text_input("Type your question here:", key="qa_input")
    if st.button("Get Answer", key="btn_qa"): 
        if question:
            with st.spinner("Generating answer..."):
                answer = qa_solver(question) 
            st.success(answer) 
        else:
            st.warning("Please enter a question first!")
with tab2:
    summary_type = st.radio(
        "Choose Summarization Type:",
        ["Short Summary", "Summarize Expander"],
        horizontal=True
    )

    text = st.text_area("Paste text here:", key="summary_input")

    if st.button("Generate", key="btn_summary"):
        if text:
            with st.spinner("Processing..."):

                if summary_type == "Short Summary":
                    output = summarize_text(text)

                elif summary_type == "Summarize Expander":
                    output = expand_text(text)

            st.success(output)

        else:
            st.warning("Please paste some text first!")

with tab3: 
    sub_tab1, sub_tab2 = st.tabs(["Career Advice", "Skill Recommendations"])

    with sub_tab1:  
        career_question = st.text_input("Type your career question here:", key="career_advice_input")  
        if st.button("Get Career Advice", key="btn_advice"): 
            if career_question: 
                with st.spinner("Generating career advice..."): 
                    answer = career_guidance(career_question, subfeature="advice") 
                st.success(answer) 
            else:
                st.warning("Please enter a question first!")  
    with sub_tab2:
        skill_question = st.text_input("Type your desired job/role here:", key="career_skills_input") 
        if st.button("Get Skill Recommendations", key="btn_skills"):  
            if skill_question:
                with st.spinner("Generating skill recommendations..."): 
                    answer = career_guidance(skill_question, subfeature="skills")
                st.success(answer)
            else:
                st.warning("Please enter a job/role first!")
