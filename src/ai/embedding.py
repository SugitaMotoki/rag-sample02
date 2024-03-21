import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), ".."))
from config import OPENAI_API_KEY

from langchain_openai import OpenAIEmbeddings


def get_embedding():
    return OpenAIEmbeddings(api_key=OPENAI_API_KEY)
