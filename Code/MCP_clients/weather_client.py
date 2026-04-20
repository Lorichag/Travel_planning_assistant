import requests

def get_weather(city):
    res = requests.post(
        "http://localhost:8001/tools/get_weather",
        json={"city": city}
    )
    return res.json()["result"]