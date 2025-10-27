# src/ingest_and_chunk.py
from pathlib import Path
from pypdf import PdfReader
import re
import json

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS_DIR = PROJECT_ROOT / "Experiments"
PDF_PATH = EXPERIMENTS_DIR / "Sample.pdf"
OUT_JSON = EXPERIMENTS_DIR / "chunks.json"

def extract_text_from_pdf(pdf_path: Path):
    reader = PdfReader(str(pdf_path))
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        pages.append({"page": i+1, "text": text})
    return pages

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.replace('\x0c', ' ')
    return text

def chunk_text_by_words(text: str, chunk_size: int = 300, overlap: int = 50):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start = end - overlap
        if start < 0:
            start = 0
    return chunks

def run(pdf_path: Path = PDF_PATH, out_json: Path = OUT_JSON):
    pages = extract_text_from_pdf(pdf_path)
    all_chunks = []
    for p in pages:
        txt = clean_text(p["text"])
        if not txt:
            continue
        p_chunks = chunk_text_by_words(txt, chunk_size=300, overlap=50)
        for idx, c in enumerate(p_chunks):
            all_chunks.append({
                "page": p["page"],
                "chunk_id": f"p{p['page']}_c{idx+1}",
                "text": c
            })
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(all_chunks)} chunks -> {out_json}")

if __name__ == "__main__":
    run()
