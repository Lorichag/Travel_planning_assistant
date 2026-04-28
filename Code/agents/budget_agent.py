from config.llm import client
from MCP_clients.cost_client import estimate_flight, estimate_hotel
from .extract_destination import extract_destination_llm
import json

# tools for budget agent
tools_budget = [
    {
        "type": "function",
        "function": {
            "name": "estimate_flight",
            "description": "Estimate flight price to a destination",
            "parameters": {
                "type": "object",
                "properties": {
                    "destination": {"type": "string"},
                    "nights": {"type": "integer"}
                },
                "required": ["destination"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "estimate_hotel",
            "description": "Estimate hotel price per night",
            "parameters": {
                "type": "object",
                "properties": {
                    "destination": {"type": "string"}
                },
                "required": ["destination"],
                "additionalProperties": False
            }
        }
    }
]

tool_functions_budget = {
    "estimate_flight": estimate_flight,
    "estimate_hotel": estimate_hotel,
}

def run_budget(itinerary):

    messages = [
        {
            "role": "system",
            "content": """
            You are a budget planner. 
            You can use cost estimation tools:
            - estimate_flight who just needs ONE parameter: the city of the destination as input and gives an estimation of the flight cost for this city
            - estimate_hotel who just needs ONE parameter: the city of the destination as input not the number of nights and gives the price for one night in a hotel

             Your goal:
            - give the price for the flight for the destination in the itinerary
            - give the price for the hotel for the destination in the itinerary
            - add an estimation of the activities cost based on the destination and the user request
            - give a final estimation of the total cost of the trip
            """
        },
        {
            "role": "user",
            "content": f"""
            Estimate total cost based on:

            {itinerary}

            Provide a breakdown of flight and hotel costs, and a final total.

            """
        }
    
    ]
    while True:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            tools=tools_budget,
            tool_choice="auto"
        )

        message = response.choices[0].message

        # 🧠 CAS 1 : appel de tool
        if message.tool_calls:

            messages.append(message)

            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)

                arguments = clean_arguments(function_name, arguments)

                print(f"💰 Tool called: {function_name} with {arguments}")

                # sécurité
                if function_name not in tool_functions_budget:
                    continue

                function = tool_functions_budget[function_name]
                result = function(**arguments)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })

        else:
            # 🧠 réponse finale
            return message.content

def clean_arguments(function_name, arguments):

    if function_name == "estimate_flight":
        return {
            "destination": arguments.get("destination")
        }

    if function_name == "estimate_hotel":
        return {
            "destination": arguments.get("destination")
        }

    if function_name == "estimate_total_cost":
        return {
            "destination": arguments.get("destination"),
            "nights": arguments.get("nights", 5)
        }

    return arguments