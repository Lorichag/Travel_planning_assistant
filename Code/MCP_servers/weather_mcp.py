from fastmcp import FastMCP

mcp = FastMCP("WeatherServer")

@mcp.tool()
def get_weather(city: str):
    city = city.strip().title()

    data = {
        # Europe
        "Rome": "Sunny 25°C",
        "Paris": "Cloudy 18°C",
        "London": "Rainy 15°C",
        "Berlin": "Windy 17°C",
        "Madrid": "Sunny 28°C",
        "Barcelona": "Sunny 24°C",

        # Amérique du Nord
        "New York": "Cloudy 20°C",
        "Los Angeles": "Sunny 27°C",
        "Toronto": "Rainy 16°C",
        "Mexico City": "Sunny 22°C",

        # Amérique du Sud
        "Rio de Janeiro": "Hot 30°C",
        "Buenos Aires": "Mild 21°C",
        "Santiago": "Sunny 23°C",

        # Asie
        "Tokyo": "Humid 26°C",
        "Seoul": "Cloudy 19°C",
        "Beijing": "Sunny 24°C",
        "Bangkok": "Hot 32°C",
        "Dubai": "Very Hot 38°C",

        # Afrique
        "Cairo": "Hot 35°C",
        "Cape Town": "Windy 20°C",
        "Marrakech": "Sunny 33°C",

        # Océanie
        "Sydney": "Sunny 22°C",
        "Melbourne": "Cloudy 19°C",
        "Auckland": "Rainy 17°C"
    }
    return data.get(city, "Unknown")