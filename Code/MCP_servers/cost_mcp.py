from fastmcp import FastMCP

mcp = FastMCP("CostServer")

@mcp.tool()
def estimate_flight(destination: str):
    """
    Estimate flight price for a given destination.
    """
    destination = destination.strip().title()

    prices = {
        # Europe
        "Rome": 150,
        "Paris": 200,
        "London": 220,
        "Berlin": 180,
        "Madrid": 170,
        "Barcelona": 180,

        # North America
        "New York": 500,
        "Los Angeles": 650,
        "Toronto": 450,
        "Mexico City": 550,

        # South America
        "Rio De Janeiro": 800,
        "Buenos Aires": 900,
        "Santiago": 850,

        # Asia
        "Tokyo": 900,
        "Seoul": 850,
        "Beijing": 750,
        "Bangkok": 700,
        "Dubai": 600,

        # Africa
        "Cairo": 400,
        "Cape Town": 950,
        "Marrakech": 300,

        # Oceania
        "Sydney": 1200,
        "Melbourne": 1150,
        "Auckland": 1300
    }
    return prices.get(destination, 120)


@mcp.tool()
def estimate_hotel(destination: str):
    """
    Estimate hotel price per night for a given destination.
    """
    destination = destination.strip().title()

    prices = {
        # Europe
        "Rome": 80,
        "Paris": 120,
        "London": 150,
        "Berlin": 90,
        "Madrid": 85,
        "Barcelona": 100,

        # North America
        "New York": 200,
        "Los Angeles": 180,
        "Toronto": 140,
        "Mexico City": 90,

        # South America
        "Rio De Janeiro": 110,
        "Buenos Aires": 95,
        "Santiago": 100,

        # Asia
        "Tokyo": 130,
        "Seoul": 110,
        "Beijing": 90,
        "Bangkok": 70,
        "Dubai": 160,

        # Africa
        "Cairo": 60,
        "Cape Town": 120,
        "Marrakech": 80,

        # Oceania
        "Sydney": 170,
        "Melbourne": 150,
        "Auckland": 140
    }
    return prices.get(destination, 70)
