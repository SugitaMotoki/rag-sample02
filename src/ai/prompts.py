from langchain_core.prompts import (
    ChatPromptTemplate,
)

default_role = "あなたは素晴らしいAIアシスタントです。"
default_task = "以下の文脈のみに基づいて、質問に回答してください。"


def get_suffix_prompt(suffix: str):
    return ChatPromptTemplate.from_template(
        f"""
        {default_role}
        {default_task}
        ただし、語尾に必ず「{suffix}」を付けてください。

        # 文脈
        {{context}}

        # 質問
        {{input}}
    """
    )


def get_prompt():
    return ChatPromptTemplate.from_template(
        f"""
        {default_role}
        {default_task}

        # 文脈
        {{context}}

        # 質問
        {{input}}
    """
    )
