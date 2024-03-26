import json
import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ".."))

from interfaces.datatypes import CallApiContextParams


def judge(required_document_ids: set, document_ids: set, allow_excess: bool):

    # 不足しているドキュメント
    deficiency = required_document_ids.difference(document_ids)
    # 過剰なドキュメント
    excess = document_ids.difference(required_document_ids)

    if len(deficiency) != 0:
        # 不足している
        return json.dumps(
            {
                "pass": False,
                "score": 1 - (len(deficiency) / len(required_document_ids)),
                "reason": f"ID：{deficiency}のドキュメントが不足しています。",
            },
            ensure_ascii=False,
        )
    elif not allow_excess:
        return json.dumps(
            {
                "pass": len(excess) == 0,
                "score": 1 - (len(excess) / len(document_ids)),
                "reason": f"ID：{excess}のドキュメントが余分です。",
            },
            ensure_ascii=False,
        )
    else:
        return json.dumps({"pass": True, "score": 1.0, "reason": ""})


def main():
    if len(sys.argv) >= 3:
        output: str = sys.argv[1]
        context: CallApiContextParams = json.loads(sys.argv[2])
    else:
        raise ValueError("Model output and context are expected from promptfoo.")

    # Retrieverが取得したドキュメント
    documents = json.loads(output)
    document_ids = set([int(document["metadata"]["id"]) for document in documents])

    # Retriever取得すべきドキュメントのID一覧
    required_document_ids = set(context["vars"]["required_document_ids"])
    # 余分なドキュメントを許すか
    allow_excess = context["vars"]["allow_excess"]

    return judge(required_document_ids, document_ids, allow_excess)


print(main())

# print(judge(set([1,2]), set([1,2]), False), 1.0)
# print(judge(set([1,2]), set([1,2]), True), 1.0)
# print(judge(set([1,2]), set([1,2,3]), False), 0.6)
# print(judge(set([1,2]), set([1,2,3]), True), 1.0)
# print(judge(set([1,2]), set([1,2,3,4]), False), 0.5)
# print(judge(set([1,2]), set([1,2,3,4]), True), 1.0)
# print(judge(set([1,2]), set([1]), False), 0.5)
# print(judge(set([1,2]), set([1]), True), 0.5)
# print(judge(set([1,2]), set([2]), False), 0.5)
# print(judge(set([1,2]), set([2]), True), 0.5)
# print(judge(set([1,2]), set([3]), False), 0.0)
# print(judge(set([1,2]), set([3]), True), 0.0)
# print(judge(set([1,2,3]), set([1,2,3,4]), False), 0.75)
# print(judge(set([1,2,3]), set([1,2,3,4]), True), 1.0)
