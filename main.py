import streamlit as st
from my_crew_config import create_crew
from tools import JDSearchTool
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# Custom CSS for style
st.markdown("""
    <style>
        .main-title { font-size:2.5em; font-weight:bold; color:#2E86C1; }
        .subtitle { font-size:1.2em; color:#117A65; }
        .footer { color: #888; font-size: 0.9em; margin-top: 2em; }
        .stButton>button { background-color: #2E86C1; color: white; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🤖 Financial Services Job Role Q&A</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask any question about financial services job roles and get expert answers based on real job descriptions.</div>', unsafe_allow_html=True)

with st.form("qa_form"):
    query = st.text_input("❓ Ask a question about financial services job roles:")
    submitted = st.form_submit_button("Get Answer")

if submitted and query:
    retriever = JDSearchTool()
    docs = retriever.search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    crew = create_crew(query, context)
    with st.spinner("💡 Generating answer..."):
        result = crew.kickoff()

    st.success("✅ Answer:")
    st.write(getattr(result, "raw", result))

    with st.expander("See retrieved job description context"):
        for i, doc in enumerate(docs, 1):
            st.markdown(f"**Context {i}:**\n{doc.page_content}")

st.markdown('<div class="footer">Powered by <b>AI Champions Bootcamp Agents</b></div>', unsafe_allow_html=True)
