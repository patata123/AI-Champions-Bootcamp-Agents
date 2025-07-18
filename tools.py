from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from crewai.tools import tool
from firecrawl.firecrawl import FirecrawlApp

class JDSearchTool:
    def __init__(self, persist_directory="chroma_db"):
        self.vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=OpenAIEmbeddings(model="text-embedding-3-small")
        )

    def search(self, query, k=3):
        return self.vectorstore.similarity_search(query, k=k)


@tool("Custom Firecrawl Scraper")
def firecrawl_scrape(url: str) -> str:
    """Scrapes content from a URL using the Firecrawl API and returns markdown output.
    """
    try:
        if not url:
            return "Missing 'url' parameter."

        app = FirecrawlApp()
        result = app.scrape_url(url, formats=["markdown"])
        return str(result)

    except Exception as e:
        return f"Scraping failed: {str(e)}"