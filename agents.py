from crewai import Agent
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

retriever_agent = Agent(
    role="JD Retriever",
    goal="Find relevant job descriptions for a given question",
    backstory="Expert at searching through job descriptions in the financial services sector.",
    tools=[],
    llm=llm
)

qa_agent = Agent(
    role="Question Answerer",
    goal="Answer user questions using retrieved job descriptions",
    backstory="Experienced HR analyst in the financial services industry.",
    tools=[],
    llm=llm
)
