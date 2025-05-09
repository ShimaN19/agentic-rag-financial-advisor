
"""Very lightweight planning module that decides whether to use RAG or purely chat history."""
from typing import List

class Planner:
    def decide(self, query: str, chat_history: List[str]) -> str:
        lowered = query.lower()
        if any(term in lowered for term in ["stock", "invest", "etf", "portfolio", "bond", "market"]):
            return "rag"
        return "chat_history"
