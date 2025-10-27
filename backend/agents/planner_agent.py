def generate_plan(query: str):
    """
    A simple planner agent that interprets what the user is asking
    and decides what the system should do next.
    """

    q_lower = query.lower()

    if "stock" in q_lower:
        return "Plan: Fetch stock fundamentals, recent news, and risk indicators."
    
    elif "mutual fund" in q_lower or "mf" in q_lower:
        return "Plan: Retrieve mutual fund performance, holdings, and risk assessment."
    
    elif "finance" in q_lower or "investment" in q_lower:
        return "Plan: Provide general personal finance insights and recommendations."
    
    else:
        return "Plan: Perform RAG search for general financial information."
