import streamlit as st
from my_crew_config import create_scrape_crew
import streamlit as st  
from utility import check_password  
import pandas as pd
import io

# Check if the password is correct.  
if not check_password():  
    st.stop()

# Custom CSS for style
st.markdown("""
    <style>
        .main-title { font-size:2.5em; font-weight:bold; color:#2E86C1; }
        .subtitle { font-size:1.2em; color:#117A65; }
        .footer { color: #888; font-size: 0.9em; margin-top: 2em; }
        .stButton>button { background-color: #2E86C1; color: white; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💼 Financial Services Job Role Salary</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Get up-to-date salary data for any financial services job role in Singapore.</div>', unsafe_allow_html=True)

with st.form("salary_form"):
    job_role = st.text_input("🔎 Enter a financial services job role (e.g., Auditor, Analyst):")
    submitted = st.form_submit_button("Get Salary Data")

if submitted and job_role:
    url = f"https://www.mycareersfuture.gov.sg/search?search={job_role}"
    crew = create_scrape_crew(url)
    with st.spinner("🔄 Scraping salary data..."):
        result = crew.kickoff()

    st.success("✅ Salary Data:")
    # Try to display as a table if possible
    if hasattr(result, "raw") and isinstance(result.raw, str) and result.raw.strip().startswith("|"):
        # Try to parse Markdown table to DataFrame
        try:
            df = pd.read_csv(io.StringIO(result.raw), sep="|", engine="python", skipinitialspace=True)
            # Drop empty columns from Markdown parsing
            df = df.loc[:, ~df.columns.str.strip().eq("")]
            st.dataframe(df)
        except Exception:
            st.markdown(result.raw)
    else:
        st.write(getattr(result, "raw", result))

    with st.expander("See raw scraped data"):
        st.write(result)

st.markdown('<div class="footer">Powered by <b>AI Champions Bootcamp Agents</b> | Data from <a href="https://www.mycareersfuture.gov.sg/" target="_blank">MyCareersFuture</a></div>', unsafe_allow_html=True)