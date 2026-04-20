from fastapi import FastAPI
from .weather_mcp import get_weather

app = FastAPI()

@app.post("/tools/get_weather")
def weather_endpoint(payload: dict):
    city = payload.get("city")
    return {"result": get_weather(city)}