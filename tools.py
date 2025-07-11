from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

class JDSearchTool:
    def __init__(self, persist_directory="chroma_db"):
        self.vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=OpenAIEmbeddings(model="text-embedding-3-small")
        )

    def search(self, query, k=3):
        return self.vectorstore.similarity_search(query, k=k)
