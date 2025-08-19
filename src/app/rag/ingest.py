from pathlib import Path
import pandas as pd
from sentence_transformers import SentenceTransformer
from config import settings
from chunk import chunk_text

model = SentenceTransformer(settings.EMB_MODEL)
def ingest_directory(data_dir: str, out_parquet: str):
    rows = []
    for p in Path(data_dir).rglob("*.txt"):
        text = p.read_text(encoding="utf-8", errors = 'ignore')
        for i, chunk in enumerate(chunk_text(text, 512)):
            rows.append({'docs':p.name, "chunk_id": i, 'text': chunk})
    df = pd.DataFrame(rows)
    df.to_parquet(out_parquet,index=False)
        