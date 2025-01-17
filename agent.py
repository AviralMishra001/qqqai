from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.python import PythonTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import streamlit as st


st.set_page_config(
    page_title="Multimodal AI Agent",
    page_icon="🌐",
    layout="wide"
)
st.title("Multimodal AI Agent 🌐🧐🔍")
st.header("Powered by Mistral AI ")


st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_resource
def initialize_agent():
    return Agent(
        name="AI Agentic RAG",
        model=Groq(id="mixtral-8x7b-32768"),
        tools=[DuckDuckGo, YFinanceTools, PythonTools],
        markdown=True,
    )

multimodal_agent=initialize_agent()
col1, col2 = st.columns([4, 1])

with col1:
    question = st.text_area(label="Question", help="Write your question here")

with col2:
    uploaded_file = st.file_uploader("", type=["txt", "pdf", "jpg", "png", "mp4"], label_visibility="collapsed")


if st.button("🔍 Analyze Query", key="analyze_query_button"):
        if not question:
            st.warning("Please enter a question or ask about financial queries.")
        else:
             try:
                  with st.spinner("Processing the query...."):
                       file_info= f"File'{uploaded_file.name}' has been uploaded. \n" if uploaded_file else ""
                       analysis_prompt=(
                            f"""
                            {file_info}
                            Analyze the uploaded file for content and context(if provided).
                            Respond to the following query using file insights(if any) and supplementary web research:
                            {question}

                            Provide a detailed, user-friendly, and actionable response.
                            """
                       )
                       response= multimodal_agent.run(analysis_prompt)
                  st.subheader("Analysis Result")
                  st.markdown(response.content)     
             except Exception as error:
                  st.error(f"An error occurred during analysis: {error}")



