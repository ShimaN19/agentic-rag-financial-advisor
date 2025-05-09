# Agentic RAG Financial Advisor Chatbot

This repository provides a modular and extensible prototype for an agentic, multi-tool Retrieval-Augmented Generation (RAG) chatbot tailored for virtual financial advisory applications. Developed to simulates a pipeline where agentic reasoning governs dynamic routing between context-aware tools such as Q&A engines, summarizers, and retrievers.

The codebase serves both as a research artifact and an instructional demo, showcasing advanced techniques in agent orchestration, tool selection, and hybrid LLM integration (OpenAI, Gemini, Anthropic). The code is framework agnostic (pure Python plus LangChain primitives) so you can swap in your own vector store, LLM, or planner with zero changes to the UI. It showcases a modular architecture in which:

1. Planning – A lightweight Planner decides at run‑time whether to call the RAG pipeline or rely on recent chat history.  
2. Retrieval – A FAISS‑backed Retriever provides high‑recall, low‑latency access to an embedded knowledge base.  
3. Generation – The RAGPipeline composes context‑rich prompts for an LLM (OpenAI GPT‑4o by default) and streams an answer.  
4. Orchestration – A minimal Gradio ChatInterface exposes the agent behind a single app.py entry‑point.



## ✨ Key Features

- **Agentic Planning Logic**  
  A lightweight planner determines—based on natural language intent—whether to retrieve knowledge, summarize prior conversation, or answer contextually.

- **Multi-LLM Backend Compatibility**  
  Integrates OpenAI (GPT-4), Gemini, and Claude for tool diversity and robustness.

- **Vector-Based Retrieval**  
  Uses ChromaDB with OpenAI embeddings on large-scale Wikipedia corpus to simulate financial document retrieval (e.g., regulations, FAQs, reports).

- **Instructional Notebook**  
  Includes a step-by-step walkthrough of the full agentic RAG flow, from data ingestion and vectorization to query routing and reasoning.

- **Modular, Package-Friendly Architecture**  
  Core logic is organized as a pip-installable Python package with clean module separation (`planner`, `router`, `engines`, etc.).

## 🧠 Use Case: Financial Advisor Agent

This system mimics a virtual financial assistant capable of:

- Answering investment-related queries (“What is a Roth IRA?”)
- Summarizing recent financial news or user transaction logs
- Deciding between multiple reasoning engines based on query type
- Escalating to human advisors when confidence is low

## 📁 Structure

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

## ⚡️ Quick Start

```
git clone https://github.com/<your‑handle>/agentic‑rag‑financial‑advisor.git
cd agentic‑rag‑financial‑advisor
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=<your‑key>   # optional: ANTHROPIC_API_KEY, GEMINI_API_KEY
python app.py                      # launches http://localhost:7860
```


## 📦 Installation

```bash
git clone https://github.com/your-username/agentic-rag-financial-advisor.git
cd agentic-rag-financial-advisor
pip install -e .
```


## 📚 Research Context

This prototype is part of a broader research agenda on planning-based LLM agents capable of dynamic reasoning over modular toolchains. It emphasizes low-latency decision-making, tool diversity, and practical orchestration using LangChain, vector databases, and prompt engineering.

## 📜 License

MIT License

---

For any questions or academic collaboration inquiries, please contact:  
`shima.nabiee [at] uci.edu`
