
from typing import List
from retriever import Retriever
from llm import call_llm

SYS_PROMPT = """You are FinBot, a helpful financial advisor. Use the provided CONTEXT to answer USER's question. 
If the context does not have the answer, say you don't know but can provide guidance."""

class RAGPipeline:
    def __init__(self, retriever: Retriever):
        self.retriever = retriever

    def answer(self, query: str, chat_history: List[str]) -> str:
        docs = self.retriever.retrieve(query, k=5)
        context = "\n".join(docs)
        prompt = f"""{SYS_PROMPT}\n\n### CONTEXT\n{context}\n\n### CHAT HISTORY\n{' '.join(chat_history)}\n\n### USER QUESTION\n{query}\n\n### RESPONSE"""
        resp = call_llm([{'role':'user','content':prompt}])
        return resp
