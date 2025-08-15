import streamlit as st
from utility import check_password  


# Check if the password is correct.  
if not check_password():  
    st.stop()

st.markdown("""
    <style>
        .main-title { font-size:2.5em; font-weight:bold; color:#2E86C1; }
        .section-title { font-size:1.5em; font-weight:bold; color:#117A65; margin-top:1em; }
        .footer { color: #888; font-size: 0.9em; margin-top: 2em; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📊 AI Champions Bootcamp Agents Project Overview</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Scope</div>', unsafe_allow_html=True)
st.write("""
This project leverages AI agents to answer questions about financial services job roles and provide up-to-date salary data for Singapore. 
It combines web scraping, retrieval, and question-answering capabilities in a user-friendly Streamlit interface.
""")

st.markdown('<div class="section-title">Objectives</div>', unsafe_allow_html=True)
st.write("""
- Provide concise, accurate answers to user queries about financial services job roles.
- Deliver real-time salary data for specific job roles using web scraping.
- Enable users to explore job descriptions and salary information interactively.
""")

st.markdown('<div class="section-title">Data Sources</div>', unsafe_allow_html=True)
st.write("""
- **Job Descriptions:** Retrieved from curated datasets and/or scraped from relevant job portals.
- **Salary Data:** Scraped from [MyCareersFuture Singapore](https://www.mycareersfuture.gov.sg/).
""")

st.markdown('<div class="section-title">Features</div>', unsafe_allow_html=True)
st.write("""
- **Q&A Agent:** Answers user questions based on real job descriptions.
- **Salary Scraper:** Extracts and displays salary tables for selected job roles.
- **Context Viewer:** Shows the source job descriptions used for answers.
- **Secure Access:** Password-protected pages for authorized use.
- **Modern UI:** Custom styling and interactive forms for seamless user experience.
""")

st.markdown('<div class="footer">Powered by <b>AI Champions Bootcamp Agents</b></div>', unsafe_allow_html=True)