from crewai import Crew
from tasks import define_tasks
from agents import retriever_agent, qa_agent

def create_crew(query, context_docs):
    tasks = define_tasks(query, context_docs)
    crew = Crew(
        agents=[retriever_agent, qa_agent],
        tasks=tasks,
        verbose=True
    )
    return crew
