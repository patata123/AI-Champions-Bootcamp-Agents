import streamlit as st

st.markdown("""
    <style>
        .main-title { font-size:2.2em; font-weight:bold; color:#2E86C1; }
        .section-title { font-size:1.3em; font-weight:bold; color:#117A65; margin-top:1em; }
        .footer { color: #888; font-size: 0.9em; margin-top: 2em; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🔬 Methodology</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Data Flow Overview</div>', unsafe_allow_html=True)

# Display your own flowchart image (replace with your actual file path)
st.image("./charts/Financial Job Q&A.drawio.png", caption="System Data Flow", use_column_width=True)

st.write("""
1. **User Query Input:**  
   Users enter questions or select job roles via the Streamlit interface.

2. **Document Retrieval:**  
   The system retrieves relevant job descriptions from curated datasets or via web scraping tools.

3. **Task Definition:**  
   The retrieved data and user query are packaged into tasks for the QA agent or scraping agent.

4. **Agent Execution:**  
   - The QA agent analyzes job descriptions and generates concise answers.
   - The web scraper agent extracts salary and company data from external sources.

5. **Result Presentation:**  
   Answers and tables are rendered in the Streamlit app, using Markdown or DataFrame components for clarity.
""")

st.markdown('<div class="section-title">Implementation Details</div>', unsafe_allow_html=True)
st.write("""
- **Agents:**  
  Implemented using the CrewAI framework, each agent has a defined role, goal, and backstory for specialized tasks.

- **Task Management:**  
  Tasks are dynamically created based on user input and routed to the appropriate agent.

- **Web Scraping:**  
  Custom tools (e.g., Firecrawl) are used to extract structured data (job title, salary, company) from job portals.

- **Environment & Security:**  
  API keys and secrets are managed via `.env` files and Streamlit's secrets management.  
  Access to the app is password-protected.

- **UI/UX:**  
  Streamlit provides a responsive interface with custom CSS for branding and usability.  
  Data tables are displayed using either Markdown or pandas DataFrames for consistency.

- **Extensibility:**  
  The modular design allows for easy addition of new agents, tools, or data sources.
""")

st.markdown('<div class="section-title">Technology Stack</div>', unsafe_allow_html=True)
st.write("""
- **Python 3.10+**
- **Streamlit** for UI
- **CrewAI** for agent orchestration
- **LangChain** for LLM integration
- **Firecrawl** for web scraping
- **pandas** for data manipulation
""")

st.markdown('<div class="footer">Powered by <b>AI Champions Bootcamp Agents</b></div>', unsafe_allow_html=True)