from crewai import Task
from agents import qa_agent

def define_tasks(query, retrieved_docs):
    qa_task = Task(
        description=f"""Based on the following job descriptions, answer the question: '{query}'.

Context:
{retrieved_docs}
""",
        expected_output="A concise and accurate answer based on the job descriptions.",
        agent=qa_agent
    )

    return [qa_task]
