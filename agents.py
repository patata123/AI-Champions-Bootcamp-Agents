from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

qa_agent = Agent(
    role="Question Answerer",
    goal="Answer user questions using retrieved job descriptions",
    backstory="Experienced HR analyst in the financial services industry.",
    tools=[],
    llm=llm
)
