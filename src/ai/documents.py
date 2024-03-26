from os.path import join, dirname

from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_documents(
    chunk_size=100,
    chunk_overlap=10,
):
    csv_path = join(dirname(__file__), "..", "data", "wiki", "wiki.csv")
    loader = CSVLoader(file_path=csv_path, metadata_columns=["id"])
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n\n",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    return text_splitter.split_documents(docs)
