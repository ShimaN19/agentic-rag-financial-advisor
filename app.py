
#!/usr/bin/env python
"""Entry point to run the Agentic RAG Financial Advisor chatbot with Gradio."""

import os, pathlib, json
from typing import List
import gradio as gr

from agentic_rag_financial_advisor.retriever import Retriever
from agentic_rag_financial_advisor.planner import Planner
from agentic_rag_financial_advisor.rag_pipeline import RAGPipeline
from agentic_rag_financial_advisor.utils import clean_history

# Load some demonstration docs (toy demo). In real use, replace with your own corpus.
SAMPLE_DOCS = [
    "Diversification spreads risk across asset classes, lowering portfolio volatility.",
    "Index funds historically outperform most actively managed funds over a 10‑year horizon.",
    "The expense ratio of an ETF directly reduces investor returns and should be kept low.",
    "Time in the market beats timing the market — staying invested is key to compounding.",
    "A common rule of thumb allocates 60% to equities and 40% to bonds for balanced growth."
]

retriever = Retriever(SAMPLE_DOCS)
planner   = Planner()
rag       = RAGPipeline(retriever)

chat_history: List[str] = []
last_bot_response: str  = ""

def chat_fn(user_input: str, history: List[str] = None):
    global chat_history, last_bot_response
    history = history or []

    # Decide which pipeline to use
    mode = planner.decide(user_input, chat_history)

    if mode == "rag":
        response = rag.answer(user_input, chat_history)
    else:
        # Simple conversational response without RAG context
        response = rag.answer(user_input, chat_history)  # fallback to rag for everything in demo

    # Update history
    if last_bot_response:
        chat_history.append(f"Bot: {last_bot_response}")
    chat_history.append(f"User: {user_input}")
    last_bot_response = response
    history.append((user_input, response))
    return history

if __name__ == "__main__":
    gr.ChatInterface(
        chat_fn,
        title="Agentic RAG Financial Advisor Chatbot",
        description="Ask finance questions; the bot uses a simple agentic RAG pipeline."
    ).launch()
