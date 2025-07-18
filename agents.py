from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

qa_agent = Agent(
    role="Question Answerer",
    goal="Answer user questions using retrieved job descriptions",
    backstory="Experienced HR analyst in the financial services industry.",
    tools=[],
    llm=llm
)
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract specific information from websites",
    backstory="An expert in web scraping who can extract targeted content from web pages.",
    verbose=True,
)
