from crewai import Crew
from tasks import define_tasks
from agents import qa_agent
from tasks import define_scrape_task
from agents import web_scraper_agent
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

def create_crew(query, context_docs):
    tasks = define_tasks(query, context_docs)
    crew = Crew(
        agents=[qa_agent],
        tasks=tasks,
        verbose=True
    )
    return crew

def create_scrape_crew(url):
    tasks = define_scrape_task(url)
    crew = Crew(
        agents=[web_scraper_agent],
        tasks=tasks,
        verbose=True
    )
    return crew

def print_crew():
    print("Crew created")