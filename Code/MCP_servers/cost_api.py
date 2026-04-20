from fastapi import FastAPI
from .cost_mcp import estimate_flight, estimate_hotel

app = FastAPI()

@app.post("/tools/estimate_flight")
def flight_endpoint(payload: dict):
    return {"result": estimate_flight(payload.get("destination"))}

@app.post("/tools/estimate_hotel")
def hotel_endpoint(payload: dict):
    return {"result": estimate_hotel(payload.get("destination"))}