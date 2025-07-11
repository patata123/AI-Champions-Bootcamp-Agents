from crew import create_crew
from tools import JDSearchTool

def main():
    query = input("Ask a question about financial services job roles: ")
    retriever = JDSearchTool()
    docs = retriever.search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    crew = create_crew(query, context)
    result = crew.kickoff()

    print("\n✅ Answer:\n", result)

if __name__ == "__main__":
    main()
