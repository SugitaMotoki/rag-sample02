from ai.retrievers import get_retriever
from ai.chain import get_chain
from ai.model import get_model
from ai.prompts import get_suffix_prompt


def retriever_test():
    retriever = get_retriever("tfidf")
    docs = retriever.get_relevant_documents("田中太郎")
    for doc in docs:
        print(doc)


def chain_test():
    # chain = get_chain()
    model = get_model(temperature=0)
    prompt = get_suffix_prompt("ピカ")
    chain = get_chain(model=model, prompt=prompt)
    result = chain.invoke({
        "input": "田中太郎のプロフィールを紹介してください。"
    })
    for k,v in result.items():
        print(f"=={k}==")
        print(v)


if __name__ == "__main__":
    # retriever_test()
    chain_test()
