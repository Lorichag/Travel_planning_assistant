import requests

def estimate_flight(destination):
    res = requests.post(
        "http://localhost:8002/tools/estimate_flight",
        json={"destination": destination}
    )
    return res.json()["result"]

def estimate_hotel(destination):
    res = requests.post(
        "http://localhost:8002/tools/estimate_hotel",
        json={"destination": destination}
    )
    return res.json()["result"]
