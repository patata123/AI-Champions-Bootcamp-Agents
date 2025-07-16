import os
from crewai import Agent, Task, Crew
from crewai_tools import FirecrawlScrapeWebsiteTool
from dotenv import load_dotenv
from crewai_tools import ScrapeElementFromWebsiteTool # Retire this tool as it does not seemed to fit our usecase now 
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from crewai.tools import tool  # this is the compatible @tool decorator
import pandas as pd
import requests
import streamlit as st

if load_dotenv('.env'):
   # for local development
   OPENAI_KEY = os.getenv('OPENAI_API_KEY')
else:
   OPENAI_KEY = st.secrets['OPENAI_API_KEY']

# -----------------------
# Tools
# -----------------------

scrape_tool = FirecrawlScrapeWebsiteTool()


# -----------------------
# Agents
# -----------------------

web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract specific information from websites",
    backstory="An expert in web scraping who can extract targeted content from web pages.",
    tools=[scrape_tool],
    verbose=True,
)

# -----------------------
# Tasks
# -----------------------

scrape_task = Task(
    description="Use the web_scraper_agent tool to extract the {url} in markdown format",
    expected_output="A markdown table containing the job title, salary, and company name.",
    agent=web_scraper_agent,
)

# -----------------------
# Crew
# -----------------------

crew = Crew(
    agents=[web_scraper_agent],
    tasks=[scrape_task]
)


result = crew.kickoff(inputs={
    "url": "https://www.mycareersfuture.gov.sg/search?search=auditor",
    "query": "income by industry"
})