__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from utility import check_password  


# Check if the password is correct.  
if not check_password():  
    st.stop()

# Custom CSS for style
st.markdown("""
    <style>
        .main-title { font-size:2.5em; font-weight:bold; color:#2E86C1; }
        .subtitle { font-size:1.2em; color:#117A65; }
        .section-title { font-size:1.5em; font-weight:bold; color:#117A65; margin-top:1em; }
        .footer { color: #888; font-size: 0.9em; margin-top: 2em; }
        .stButton>button { background-color: #2E86C1; color: white; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🤖 AI Champions Bootcamp Agents</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Empowering financial services professionals with AI-driven job insights and salary data.</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Welcome!</div>', unsafe_allow_html=True)
st.write("""
This application leverages advanced AI agents to answer your questions about financial services job roles and provide up-to-date salary information for Singapore.
Explore the pages in the sidebar to:
- Ask questions about job roles and get expert answers.
- View real job descriptions and salary tables.
- Learn more about the project scope, objectives, and data sources.
""")

st.markdown('<div class="section-title">How to Use</div>', unsafe_allow_html=True)
st.write("""
1. Select a page from the sidebar (e.g., Q&A, Salary Scraper, Project Overview).
2. Enter your query or select a job role.
3. View concise answers and supporting context.
""")

st.markdown('<div class="section-title">About</div>', unsafe_allow_html=True)
st.write("""
Developed for the AI Champions Bootcamp, this project demonstrates the power of multi-agent systems in real-world HR analytics.
""")

st.markdown('<div class="footer">Powered by <b>AI Champions Bootcamp Agents</b></div>', unsafe_allow_html=True)