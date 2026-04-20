from langgraph.graph import StateGraph

from agents.research_agent import run_research
from agents.itinerary_agent import run_itinerary
from agents.budget_agent import run_budget
from agents.verification_agent import run_verification

def research_node(state):
    return {"research": run_research(state["input"])}

def itinerary_node(state):
    return {"itinerary": run_itinerary(state["research"])}

def budget_node(state):
    return {"budget": run_budget(state["itinerary"])}

def verify_node(state):
    combined = f"""
    {state['research']}
    {state['itinerary']}
    {state['budget']}
    """
    return {"final": run_verification(combined)}

def hitl_node(state):
    print("\n=== HUMAN VALIDATION ===")
    print(state["final"])

    decision = input("Approve? (yes/no): ")

    if decision == "yes":
        return state
    else:
        new_input = input("Modify your request: ")
        return {"input": new_input}

builder = StateGraph(dict)

builder.add_node("research", research_node)
builder.add_node("itinerary", itinerary_node)
builder.add_node("budget", budget_node)
builder.add_node("verify", verify_node)
builder.add_node("hitl", hitl_node)

builder.set_entry_point("research")

builder.add_edge("research", "itinerary")
builder.add_edge("itinerary", "budget")
builder.add_edge("budget", "verify")
builder.add_edge("verify", "hitl")

graph = builder.compile()