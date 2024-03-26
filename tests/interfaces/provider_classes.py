import json

from langchain_core.runnables import Runnable
from langchain_core.retrievers import BaseRetriever
from langchain_core.documents import Document

from .datatypes import (
    ProviderOptions,
    CallApiContextParams,
    TokenUsage,
    ProviderResponse,
)


class PythonProvider:
    """
    Pythonで作成されたProviderをPromptfooで使用するためのクラス
    """

    def _call_api(
        self, prompt: str, options: ProviderOptions, context: CallApiContextParams
    ) -> ProviderResponse:
        """
        Promptfooから呼ぶcall_apiの定義
        """

        return {
            "output": "This is Python Provider.",
        }

    def get_call_api(self):
        return self._call_api


class RetrieverProvider(PythonProvider):
    def __init__(self, retriever: BaseRetriever) -> None:
        self.retriever = retriever

    def _call_api(
        self, prompt: str, options: ProviderOptions, context: CallApiContextParams
    ):
        documents = self.retriever.get_relevant_documents(prompt)
        document_strings = [vars(document) for document in documents]

        return {"output": json.dumps(document_strings, ensure_ascii=False)}


class ChainProvider(PythonProvider):
    """
    - Chainを用いるProvider
    - 事前に用意したChainをコンストラクタで注入
    - yamlののprovider#config（call_apiのoptionsにあたる部分）は使用しない前提
    """

    def __init__(self, chain: Runnable):
        self.chain = chain

    def _call_api(
        self, prompt: str, options: ProviderOptions, context: CallApiContextParams
    ):
        return {
            "output": "This is Chain Provider.",
        }


class EndToEndChainProvider(ChainProvider):
    def __init__(self, chain: Runnable):
        super().__init__(chain)

    def _call_api(
        self, prompt: str, options: ProviderOptions, context: CallApiContextParams
    ):
        output = self.chain.invoke({"input": prompt})
        return {"output": output["answer"]}
