from config.llm import client
from MCP_clients.weather_client import get_weather

def run_research(user_input,history):

    history_text = "\n".join([
        f"Previous request: {h['request']}\nResult: {h['result']}"
        for h in history
    ])

    weather_info = get_weather("Rome")

    prompt = f"""
    You are a travel expert.

    Previous interactions:
    {history_text}

    User request:
    {user_input}

    Weather example:
    {weather_info}

    Take into account previous preferences and corrections.

    Suggest destinations with activities.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content