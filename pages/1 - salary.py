import streamlit as st
from crew import create_scrape_crew

st.title("Financial Services Job Role Salary")

job_role = st.text_input("Input financial services job role:")

if job_role:
    # Construct a search URL for the job role (example: MyCareersFuture Singapore)
    url = f"https://www.mycareersfuture.gov.sg/search?search={job_role}"
    crew = create_scrape_crew(url)
    with st.spinner("Scraping salary data..."):
        result = crew.kickoff(inputs={"url": url})

    st.success("✅ Salary Data:")
    st.write(getattr(result, "raw", result))