
# Agentic RAG Financial Advisor Chatbot

This repository contains a production‑ready demo of an Agentic Retrieval‑Augmented Generation (RAG) chatbot that acts as a virtual financial advisor.  
It showcases a modular architecture in which:

1. Planning – A lightweight Planner decides at run‑time whether to call the RAG pipeline or rely on recent chat history.  
2. Retrieval – A FAISS‑backed Retriever provides high‑recall, low‑latency access to an embedded knowledge base.  
3. Generation – The RAGPipeline composes context‑rich prompts for an LLM (OpenAI GPT‑4o by default) and streams an answer.  
4. Orchestration – A minimal Gradio ChatInterface exposes the agent behind a single app.py entry‑point.

The code is framework agnostic (pure Python plus LangChain primitives) so you can swap in your own vector store, LLM, or planner with zero changes to the UI.

---

## Quick Start

```
git clone https://github.com/<your‑handle>/agentic‑rag‑financial‑advisor.git
cd agentic‑rag‑financial‑advisor
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=<your‑key>   # optional: ANTHROPIC_API_KEY, GEMINI_API_KEY
python app.py                      # launches http://localhost:7860
```

## Repository Layout

```
agentic_rag_financial_advisor/
├── __init__.py
├── config.py
├── retriever.py
├── rag_pipeline.py
├── planner.py
├── llm.py
└── utils.py
app.py
requirements.txt
README.md
```

## Extending the Demo

Component table of suggestions:

Component | Swap‑in Alternative | Reason  
Planner | GPT‑4o function‑calling, prompt‑injected ReAct, LangGraph | multi‑step reasoning  
Retriever | Chroma, Weaviate, ElasticSearch | hybrid search and scaling  
LLM | Anthropic Claude‑3, Gemini 1.5‑Pro, local Mixtral 8x7B | cost and latency

## Demo Knowledge Base

For brevity the repo ships with five toy sentences hard coded in app.py.  
Replace them with real documents such as 10‑K filings or Morningstar reports.

## License

MIT. Use at your own risk.

## Citation

```
@misc{nabiee2025agenticrag,
  author  = {Shima Nabiee},
  title   = {Agentic RAG Financial Advisor Chatbot},
  year    = {2025},
  url     = {https://github.com/ShimaN19/agentic-rag-financial-advisor}
}
```
