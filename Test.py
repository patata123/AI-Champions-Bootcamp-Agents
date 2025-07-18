from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from tools import firecrawl_scrape  # your custom tool

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

scraper_agent = Agent(
    role="Web Scraper",
    goal="Scrape job descriptions from recruitment websites",
    backstory="Expert in web scraping for HR and recruitment insights.",
    tools=[firecrawl_scrape],
    llm=llm,
    verbose=True
)

scrape_task = Task(
    description="Scrape job postings from MyCareersFuture related to 'auditor'.",
    expected_output="A markdown summary of job listings for auditor.",
    agent=scraper_agent,
    input={"url": "https://www.mycareersfuture.gov.sg/search?search=auditor"}
)

crew = Crew(
    agents=[scraper_agent],
    tasks=[scrape_task]
)

crew.kickoff()
