
"""Simple FAISS-based document retriever for the Agentic RAG Financial Advisor."""

from typing import List
from pathlib import Path
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(self, docs: List[str], model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.docs = docs
        self.index = None
        self.embeddings = None
        self.build_index()

    def build_index(self):
        self.embeddings = self.model.encode(self.docs, show_progress_bar=False, convert_to_numpy=True)
        d = self.embeddings.shape[1]
        self.index = faiss.IndexFlatIP(d)
        faiss.normalize_L2(self.embeddings)
        self.index.add(self.embeddings)

    def retrieve(self, query: str, k: int = 5) -> List[str]:
        query_vec = self.model.encode([query], convert_to_numpy=True)
        faiss.normalize_L2(query_vec)
        scores, idxs = self.index.search(query_vec, k)
        return [self.docs[i] for i in idxs[0]]
