from os.path import join, dirname, isdir

from langchain.vectorstores.faiss import FAISS
from langchain_community.retrievers import TFIDFRetriever
from langchain_core.retrievers import BaseRetriever
from .embedding import get_embedding
from .documents import get_documents

# デフォルト
embedding = get_embedding()
documents = get_documents()


def get_faiss_retriever(embedding=embedding, documents=documents):
    db_path = join(dirname(__file__), "..", "data", "wiki", "faiss")

    if isdir(db_path):
        vector_db = FAISS.load_local(
            db_path, embeddings=embedding, allow_dangerous_deserialization=True
        )
        return vector_db.as_retriever()
    else:
        vector_db = FAISS.from_documents(documents, embedding)
        vector_db.save_local(db_path)
        return vector_db.as_retriever()


def get_tfidf_retriever(documents=documents):
    db_path = join(dirname(__file__), "..", "data", "wiki", "tfidf")

    if isdir(db_path):
        return TFIDFRetriever.load_local(db_path, allow_dangerous_deserialization=True)
    else:
        retriever = TFIDFRetriever.from_documents(documents)
        retriever.save_local(db_path)
        return retriever


def get_retriever(
    retriever_type="faiss", embedding=embedding, documents=documents
) -> BaseRetriever:
    if retriever_type == "faiss":
        return get_faiss_retriever(embedding=embedding, documents=documents)
    elif retriever_type == "tfidf":
        return get_tfidf_retriever(documents=documents)
    # elif (retriever_type == "hybrid"):
    #     return get_hybrid_retriever()
    else:
        raise ValueError("unknown retriever type")
