# 💸 FINSAGE.AI — Intelligent Financial Insights Chatbot

Finsage.AI is an AI-powered chatbot that provides **personalized insights** about **stocks, mutual funds, and personal finance** using **Retrieval-Augmented Generation (RAG)** and intelligent agents.

---

## 🚀 Problem Statement

Retail investors often face information overload and confusion while analyzing stocks, mutual funds, or financial news.  
Finsage.AI aims to **bridge this gap** by providing:
- Simplified insights from **authentic financial sources**.
- **Live stock and market data**.
- **Summarized news** and **AI-backed reasoning**.
- Actionable suggestions (Buy / Hold / Sell) with clear justifications.

---

## 🎯 Key Features

- 🧠 **LLM + RAG integration:** Combines context retrieval and reasoning.
- 📰 **Live financial news summaries:** Fetches and condenses real-time market news.
- 💹 **Stock fundamentals retrieval:** Pulls key ratios, market trends, and data via APIs.
- 💬 **Conversational agent:** Answers user queries about stocks, mutual funds, and finance.
- 🧩 **Modular FastAPI backend:** Cleanly separated routes and services.
- ⚡ **Future integration:** Frontend (React) + backend (FastAPI) + agents (LangChain).

---

## 🏗️ Project Structure

Mini2.0/
│
├── backend/                  # FastAPI backend for RAG & data agents
│   ├── agents/               # Planner, retriever, analyzer agents
│   ├── routers/              # API route handlers
│   ├── services/             # Logic for data, news, summarization
│   ├── main.py               # FastAPI entrypoint
│   └── __init__.py
│
├── experiments/              # RAG and LLM experimentation notebooks
│   ├── rag_pipeline.ipynb
│   └── Sample.pdf
│
├── .gitignore                # Ignored cache/models/env folders
├── requirements.txt          # Python dependencies
└── README.md                 # (This file)

---

## 🧰 Tech Stack

| Layer | Tools Used |
|-------|-------------|
| Backend | FastAPI, Uvicorn |
| AI / NLP | SentenceTransformers, HuggingFace Transformers |
| RAG Storage | ChromaDB |
| News & Data | Requests, YahooFinance APIs |
| Deployment | Git + GitHub + Render (Planned) |

---

## ⚙️ How It Works

1. **User enters a query** (e.g., "Should I invest in Tata Motors?")  
2. **Query parser** extracts key entities (e.g., Tata Motors → Stock).  
3. **Retriever Agent** fetches related news + financial data.  
4. **Analyzer Agent** generates insights using pretrained models.  
5. **Response Composer** returns a summary with reasoning and warnings.

---

## 👥 Team

- **Aryan Pratik**   
- **Aditya Gupta** 

---

## 🧾 License
This project is developed as part of **Mini Project 2.0 (2025)**.  
All code is for educational and research purposes only.
