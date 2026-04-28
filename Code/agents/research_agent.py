from config.llm import client
from MCP_clients.weather_client import get_weather
from .extract_destination import extract_destination_llm
import json

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                },
                "required": ["city"]
            }
        }
    },
]

tool_research = {
    "get_weather": get_weather,
}

def run_research(user_input,history):

    history_text = "\n".join([
        f"Previous request: {h['request']}\nResult: {h['result']}"
        for h in history
    ])


    messages = [
        {
            "role": "system",
            "content": """
            You are a travel expert. 
            You can just use one tool:
            - get_weather : to get current weather for a city,
            the only argument is city, which should be a string just the city not the country or continent. For example "Paris" and not "Paris, France" or "Europe",
            the output is the current weather for the city, if the city is not found the output will be unknown that mean we dont know the weather for this city.

            Your goal:
            - extract the destination from the user request
            - give the weather for that destination if the city is known
            - propose some activities for this destination
            """
        },
        {
            "role": "user",
            "content": f"""
            Previous interactions:
            {history_text}

            User request:
            {user_input}
            """
        }
    ]

    while True:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        message = response.choices[0].message

        # 🧠 CAS 1 : le modèle veut appeler un tool
        if message.tool_calls:

            messages.append(message)

            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                if function_name not in tool_research:
                    print(f"⚠️ Unknown tool: {function_name} → ignored")
                    continue
                arguments = json.loads(tool_call.function.arguments)

                print(f"🔧 Tool called: {function_name} with {arguments}")

                function = tool_research[function_name]
                result = function(**arguments)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })

        else:
            # 🧠 CAS 2 : réponse finale
            return message.content