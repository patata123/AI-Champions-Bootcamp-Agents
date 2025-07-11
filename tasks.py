from crewai import Task
from agents import retriever_agent, qa_agent

def define_tasks(query, retrieved_docs):
    retrieval_task = Task(
        description=f"Find job descriptions relevant to the question: '{query}'",
        expected_output="A list of 2-3 relevant job descriptions",
        agent=retriever_agent
    )

    qa_task = Task(
        description=f"""Based on the following job descriptions, answer the question: '{query}'.

Context:
{retrieved_docs}
""",
        expected_output="A concise and accurate answer based on the job descriptions.",
        agent=qa_agent
    )

    return [retrieval_task, qa_task]
    