# src/retriever.py
from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from typing import Dict, Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CHROMA_DIR = PROJECT_ROOT / "chroma_db"
COLLECTION_NAME = "finsage_docs"

_model = None
_client = None
_collection = None

def _init():
    global _model, _client, _collection
    if _model is None:
        _model = SentenceTransformer('all-MiniLM-L6-v2')
    if _client is None:
        _client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=str(CHROMA_DIR)))
    if _collection is None:
        _collection = _client.get_collection(name=COLLECTION_NAME)
    return _model, _collection

def query(query_text: str, top_k: int = 3) -> Dict[str, Any]:
    model, collection = _init()
    q_emb = model.encode([query_text])[0].astype("float32")
    res = collection.query(
        query_embeddings=[q_emb.tolist()],
        n_results=top_k,
        include=["documents", "metadatas", "distances", "ids"]
    )
    # Chroma returns nested lists
    out = []
    for i, doc in enumerate(res["documents"][0]):
        out.append({
            "id": res["ids"][0][i],
            "document": doc,
            "metadata": res.get("metadatas", [[]])[0][i] if "metadatas" in res else {},
            "distance": res.get("distances", [[]])[0][i] if "distances" in res else None
        })
    return {"query": query_text, "results": out}
