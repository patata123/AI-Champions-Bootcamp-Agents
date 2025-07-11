import streamlit as st
from crew import create_crew
from tools import JDSearchTool

st.title("Financial Services Job Role Q&A")

query = st.text_input("Ask a question about financial services job roles:")

if query:
    retriever = JDSearchTool()
    docs = retriever.search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    crew = create_crew(query, context)
    with st.spinner("Generating answer..."):
        result = crew.kickoff()

    st.success("✅ Answer:")
    st.write(result)
