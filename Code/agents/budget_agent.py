from config.llm import client
from MCP_clients.cost_client import estimate_flight, estimate_hotel

def run_budget(itinerary):

    flight = estimate_flight("Rome")
    hotel = estimate_hotel("Rome")

    prompt = f"""
    Estimate total cost based on:

    {itinerary}

    Flight: {flight}
    Hotel per night: {hotel}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content