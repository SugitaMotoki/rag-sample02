import sys
from os.path import join, dirname
sys.path.append(join(dirname(__file__), "..", ".."))

from tests.interfaces.provider_classes import RetrieverChainProvider
from src.ai.chain import get_chain
from src.ai.retrievers import get_retriever

retriever = get_retriever("faiss")
chain = get_chain(retriever=retriever)

provider = RetrieverChainProvider(chain=chain)
call_api = provider.get_call_api()
