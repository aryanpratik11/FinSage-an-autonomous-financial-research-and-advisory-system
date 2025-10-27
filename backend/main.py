# backend/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from src.retriever import query as retriever_query
from src.agents import stock_agent, mutual_fund_agent

app = FastAPI(title="FinSage RAG Backend", version="0.1")

class QueryRequest(BaseModel):
    question: str
    top_k: Optional[int] = 3

class StockRequest(BaseModel):
    symbol: str

@app.get("/")
def root():
    return {"service": "FinSage RAG backend", "status": "ok"}

@app.post("/retrieve")
def retrieve(req: QueryRequest):
    try:
        res = retriever_query(req.question, top_k=req.top_k)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/agent/stock")
def get_stock(req: StockRequest):
    try:
        res = stock_agent(req.symbol)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/agent/mutualfund")
def mutualfund(req: QueryRequest):
    try:
        res = mutual_fund_agent(req.question, top_k=req.top_k)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate")
def generate(req: QueryRequest):
    """
    Placeholder generation endpoint.
    Steps you can implement here:
      1. Retrieve top-k chunks (use retriever_query)
      2. Construct a prompt: system + context (top chunks) + user question
      3. Call an LLM (OpenAI / local HF) to generate an answer
    For now this returns 'context' so your LLM team can plug in the model easily.
    """
    try:
        retrieved = retriever_query(req.question, top_k=req.top_k)
        # Build context text -> concatenated top chunks
        context_texts = [r["document"] for r in retrieved["results"]]
        # Return the context; groupmate will replace this with LLM output.
        return {
            "question": req.question,
            "context": context_texts,
            "note": "Plug your LLM call here in /generate to produce a final answer using context."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
