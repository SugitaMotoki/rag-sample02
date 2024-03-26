import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ".."))

from tests.interfaces.provider_classes import RetrieverProvider
from src.ai.retrievers import get_retriever

retriever = get_retriever("tfidf")

provider = RetrieverProvider(retriever=retriever)
call_api = provider.get_call_api()
