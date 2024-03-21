from langchain_core.documents import Document
import json

documents = [
    Document(
        page_content="id: 1\npageid: 1\ntitle: 田中太郎\nsection: プロフィール/年齢\ntext: 田中太郎は35才である。",
        metadata={
            "source": "/home/motok/work/nri/wiki_rag/src/ai/../data/wiki/wiki.csv",
            "row": 0,
        },
    ),
    Document(
        page_content="id: 3\npageid: 1\ntitle: 田中太郎\nsection: プロフィール/性別\ntext: 田中太郎は男性である。",
        metadata={
            "source": "/home/motok/work/nri/wiki_rag/src/ai/../data/wiki/wiki.csv",
            "row": 2,
        },
    ),
    Document(
        page_content="id: 10\npageid: 1\ntitle: 鈴木次郎\nsection: プロフィール/年齢\ntext: 鈴木次郎は16才である。",
        metadata={
            "source": "/home/motok/work/nri/wiki_rag/src/ai/../data/wiki/wiki.csv",
            "row": 9,
        },
    ),
    Document(
        page_content="id: 4\npageid: 1\ntitle: 田中太郎\nsection: 関係/鈴木花子\ntext: 田中太郎は鈴木花子の先生である。",
        metadata={
            "source": "/home/motok/work/nri/wiki_rag/src/ai/../data/wiki/wiki.csv",
            "row": 3,
        },
    ),
]

for doc in documents:
    # print(doc.page_content)
    # print(json.dumps(doc.metadata))
    # print(vars(doc))
    pass

r = [vars(document) for document in documents]
# print(r)

result = {
    "output": json.dumps(r, ensure_ascii=False)
}

print(result)

