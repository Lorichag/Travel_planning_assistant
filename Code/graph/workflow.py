from langgraph.graph import StateGraph

from agents.research_agent import run_research
from agents.itinerary_agent import run_itinerary
from agents.budget_agent import run_budget
from agents.verification_agent import run_verification
from config.email import send_email
from config.email import format_travel_email

def research_node(state):
    result = run_research(state["input"],state.get("history", []))
    print("RESEARCH:", result)
    return {**state,"research": result}

def itinerary_node(state):
    result = run_itinerary(state["research"])
    print("ITINERARY:", result)
    return {**state,"itinerary": result}

def budget_node(state):
    result = run_budget(state["itinerary"])
    print("BUDGET:", result)
    return {**state,"budget": result}

def verify_node(state):

    research = state.get("research", "")
    itinerary = state.get("itinerary", "")
    budget = state.get("budget", "")

    combined = f"""
    Research:
    {research}

    Itinerary:
    {itinerary}

    Budget:
    {budget}
    """

    return {**state, "final": run_verification(combined)}

def hitl_node(state):
    print("\n=== HUMAN VALIDATION ===")
    print(state["final"])

    decision = input("Approve? (yes/no): ")

    if decision.lower() == "yes":

        #mail = input("Do you want to receive the plan by email? (yes/no): ")
        #if mail.lower() == "yes":
            # doesn't work
            #email = input("Enter your email: ")

            #content = format_travel_email(state)

            #send_email(
            #    to_email=email,
            #    subject="Your Travel Plan ✈️",
            #    content=content
            #)
            #print("📧 Sending email...")

        return {"final": state["final"], "approved": True}
    else:
        new_input = input("Modify your request: ")
        request = state.get("input", "unknown")
        return {
            "input": new_input,
            "history": state.get("history", []) + [
                {
                    "request": request,
                    "result": state["final"]
                }
            ],
            "approved": False
        }

def route_after_hitl(state):
    if state.get("approved"):
        return "end"
    else:
        return "research"

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
builder.add_conditional_edges(
    "hitl",
    route_after_hitl,
    {
        "research": "research",
        "end": "__end__"
    }
)

graph = builder.compile()