import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), ".."))
from config import OPENAI_API_KEY

from langchain_openai import ChatOpenAI


def get_model(model_name: str = "gpt-3.5-turbo", temperature: float = 0):
    return ChatOpenAI(api_key=OPENAI_API_KEY, model=model_name, temperature=temperature)
