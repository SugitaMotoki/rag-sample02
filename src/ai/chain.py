from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from .prompts import get_prompt
from .model import get_model
from .embedding import get_embedding
from .documents import get_documents
from .retrievers import get_retriever

# デフォルト値
prompt = get_prompt()
model = get_model()
embedding = get_embedding()
documents = get_documents()
retriever = get_retriever(
    retriever_type="faiss", embedding=embedding, documents=documents
)


def get_chain(model=model, retriever=retriever, prompt=prompt):
    document_chain = create_stuff_documents_chain(llm=model, prompt=prompt)
    retriever_chain = create_retrieval_chain(
        retriever=retriever, combine_docs_chain=document_chain
    )
    return retriever_chain
