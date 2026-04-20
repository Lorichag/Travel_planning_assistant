from fastmcp import FastMCP

mcp = FastMCP("WeatherServer")

@mcp.tool()
def get_weather(city: str):
    data = {
        "Rome": "Sunny 25°C",
        "Paris": "Cloudy 18°C"
    }
    return data.get(city, "Unknown")