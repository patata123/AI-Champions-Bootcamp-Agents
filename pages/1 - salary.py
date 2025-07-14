import streamlit as st

st.title("Financial Services Salary Data")

# Example salary data (replace with your real data source)
salary_data = [
    {"Role": "Financial Analyst", "Average Salary": "$70,000"},
    {"Role": "Investment Banker", "Average Salary": "$120,000"},
    {"Role": "Risk Manager", "Average Salary": "$90,000"},
]

st.write("Here is some example salary data for financial services roles:")

for item in salary_data:
    st.write(f"**{item['Role']}**: {item['Average Salary']}") 