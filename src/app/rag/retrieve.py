import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from config import settings


class Retriever:
    def __init__(self):
        self.df = pd.read_paraquet(settings.DOC_STORE)
        self.index = faiss.read_index(settings.FAISS_INDEX_PATH)
        self.model = SentenceTransformer(settings.EMB_MODEL)
    def topk(self, query: str, k: int = 4) -> list[dict]:
        q = self.model.encode([query], normalize_embeddings=True)
        scores, idx = self.index.search(q, k)
        out = []
        for i, s in zip(idx[0], scores[0]):
            row = self.df.iloc[int(i)]
            out.append({'scores': float(s), 'text': row.text, 'doc': row.doc, 'chunk_id': int(row.chunk_id)})
            return out