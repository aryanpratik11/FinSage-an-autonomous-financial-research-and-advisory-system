# src/agents.py
from typing import Dict, Any
from .retriever import query as retrieve
import yfinance as yf

def stock_agent(symbol: str) -> Dict[str, Any]:
    """
    Lightweight stock agent using yfinance (free) to fetch latest price + simple sentiment placeholder.
    """
    try:
        t = yf.Ticker(symbol)
        info = t.info if hasattr(t, "info") else {}
        hist = t.history(period="7d")
        latest_close = hist["Close"].iloc[-1] if not hist.empty else None
        return {
            "symbol": symbol,
            "latest_close": float(latest_close) if latest_close is not None else None,
            "summary": info.get("longBusinessSummary", "")[:800],
            "raw_info": {"sector": info.get("sector"), "industry": info.get("industry")}
        }
    except Exception as e:
        return {"error": str(e)}

def mutual_fund_agent(query_text: str, top_k: int = 3) -> Dict[str, Any]:
    """
    For mutual fund questions: run RAG retrieval and return the top chunks.
    Later, send these to an LLM for summarization.
    """
    retrieved = retrieve(query_text, top_k=top_k)
    # For now, simply return retrieved context. Groupmate will plug LLM here.
    return {"query": query_text, "retrieved_chunks": retrieved["results"]}
