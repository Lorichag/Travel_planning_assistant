from config.llm import client
from MCP_clients.weather_client import get_weather

def run_research(user_input):

    weather_info = get_weather("Rome")

    prompt = f"""
    You are a travel expert.

    User request:
    {user_input}

    Weather example:
    {weather_info}

    Suggest 2 destinations with activities.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content