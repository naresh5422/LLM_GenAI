import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from config import settings

emb_model = SentenceTransformer(settings.EMB_MODEL)

def build_index(parquet_path: str, index_path: str):
    """
    Build a FAISS index from a Parquet file containing text data.
    
    Args:
        parquet_path (str): Path to the Parquet file.
        index_path (str): Path to save the FAISS index.
    """
    # Load data
    df = pd.read_parquet(parquet_path)
    vecs = emb_model.encode(df['text'].tolist(), normalize_embeddings=True)
    index = faiss.IndexFlatIP(vecs.shape[1])
    index.add(np.array(vecs).astype('float32'))
    faiss.write_index(index, index_path)
    return len(df)

    