from crewai import Task
from agents import qa_agent
from agents import web_scraper_agent
from dotenv import load_dotenv
load_dotenv('.env')

def define_tasks(query, retrieved_docs):
    qa_task = Task(
        description=f"""Based on the following job descriptions, answer the question: '{query}'.

Context:
{retrieved_docs}
""",
        expected_output="A concise and accurate answer based on the job descriptions.",
        agent=qa_agent,
    )

    return [qa_task]

def define_scrape_task(url):
    scrape_task = Task(
        description=f"Use the web_scraper_agent tool to extract the {url} in markdown format",
        expected_output="A markdown table containing the job title, salary, and company name.",
        agent=web_scraper_agent,
    )
    return [scrape_task]
