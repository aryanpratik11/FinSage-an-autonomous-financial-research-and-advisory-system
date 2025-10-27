from fastapi import APIRouter
from backend.agents import planner_agent

router = APIRouter()

@router.post("/")
async def chat_with_agent(user_query: dict):
    """
    Main chatbot endpoint.
    Expects a JSON body like:
    {
        "query": "Tell me about HDFC Mutual Fund"
    }
    """
    query = user_query.get("query", "")
    
    if not query:
        return {"error": "Query cannot be empty"}
    
    # Step 1: Planner agent analyses user intent and creates a plan
    plan = planner_agent.generate_plan(query)
    
    # Step 2: For now, just return the plan (we'll later trigger retrieval & reasoning)
    return {
        "user_query": query,
        "plan_generated": plan
    }
