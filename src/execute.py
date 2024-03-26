from ai.retrievers import get_retriever
from ai.chain import get_chain
from ai.model import get_model
from ai.prompts import get_suffix_prompt
from ai.documents import get_documents


def retriever_test():
    retriever = get_retriever("faiss")
    docs = retriever.get_relevant_documents("インドネシアの主な島は？")
    for doc in docs:
        print(doc)


def chain_test():
    # chain = get_chain()
    model = get_model(temperature=0)
    prompt = get_suffix_prompt("ピカ")
    retriever = get_retriever("tfidf")
    chain = get_chain(model=model, prompt=prompt, retriever=retriever)
    result = chain.invoke({"input": "インドネシアの主な島は？"})
    for k, v in result.items():
        print(f"=={k}==")
        print(v)


if __name__ == "__main__":
    # get_documents()
    # retriever_test()
    chain_test()
