# src/build_index.py
from pathlib import Path
import json
import numpy as np
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS_DIR = PROJECT_ROOT / "Experiments"
CHUNKS_JSON = EXPERIMENTS_DIR / "chunks.json"
CHROMA_DIR = PROJECT_ROOT / "chroma_db"  # directory to persist vector DB
COLLECTION_NAME = "finsage_docs"

def load_chunks(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def build(chunks_path: Path = CHUNKS_JSON, chroma_dir: Path = CHROMA_DIR, collection_name: str = COLLECTION_NAME):
    print("Loading model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("Loading chunks...")
    chunks = load_chunks(chunks_path)
    texts = [c["text"] for c in chunks]
    ids = [c["chunk_id"] for c in chunks]
    metadatas = [{"page": c["page"]} for c in chunks]

    print("Encoding embeddings (this may take a moment)...")
    embeddings = model.encode(texts, convert_to_numpy=True)
    embeddings = embeddings.astype("float32")  # chroma expects lists/float

    # Setup Chroma client with persistence
    client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=str(chroma_dir)))
    collection = client.get_or_create_collection(name=collection_name)

    # Add data to collection
    print("Adding to Chroma collection...")
    collection.add(
        ids=ids,
        documents=texts,
        metadatas=metadatas,
        embeddings=[e.tolist() for e in embeddings]
    )

    # Persist (Chroma will persist automatically, but explicit call ensures it)
    client.persist()
    print(f"Indexed {len(ids)} chunks into Chroma collection '{collection_name}' at {chroma_dir}")

if __name__ == "__main__":
    build()
