
from typing import List, Optional
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from config import get_openai_api_key

def call_llm(messages: List, temperature: float = 0.3, max_tokens: int = 512) -> str:
    llm = ChatOpenAI(api_key=get_openai_api_key(), temperature=temperature, max_tokens=max_tokens)
    response = llm(messages)
    return response.content
