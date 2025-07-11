import pandas as pd
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
import os

# Constants
EXCEL_FILENAME = "jobsandskills-skillsfuture-skills-framework-dataset.xlsx"
EXCEL_PATH = os.path.join("job_descriptions", EXCEL_FILENAME)
COLUMN_NAME = "Job Role Description"
SECTOR_FILTER_COLUMN = "Sector"
SECTOR_FILTER_VALUE = "Financial Services"
PERSIST_DIR = "chroma_db"

def ingest_excel_column():
    if not os.path.exists(EXCEL_PATH):
        raise FileNotFoundError(f"File not found: {EXCEL_PATH}")

    df = pd.read_excel(EXCEL_PATH)

    if COLUMN_NAME not in df.columns:
        raise ValueError(f"Column '{COLUMN_NAME}' not found. Available columns: {list(df.columns)}")

    if SECTOR_FILTER_COLUMN not in df.columns:
        raise ValueError(f"Column '{SECTOR_FILTER_COLUMN}' not found. Available columns: {list(df.columns)}")

    # Filter by Sector = "financial services" (case-insensitive match)
    filtered_df = df[df[SECTOR_FILTER_COLUMN].str.lower() == SECTOR_FILTER_VALUE.lower()]
    if filtered_df.empty:
        raise ValueError(f"No job descriptions found with Sector = '{SECTOR_FILTER_VALUE}'.")

    documents = []
    for idx, row in filtered_df.iterrows():
        text = str(row[COLUMN_NAME])
        metadata = {col: str(row[col]) for col in df.columns if col != COLUMN_NAME}
        documents.append(Document(page_content=text, metadata=metadata))

    embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = Chroma.from_documents(documents, embedding=embeddings_model, persist_directory=PERSIST_DIR)
    vectorstore.persist()
    print(f"✅ Ingested {len(documents)} job descriptions for Sector = '{SECTOR_FILTER_VALUE}' into '{PERSIST_DIR}'")

if __name__ == "__main__":
    ingest_excel_column()