from fastmcp import FastMCP

mcp = FastMCP("CostServer")

@mcp.tool()
def estimate_flight(destination: str):
    """
    Estimate flight price for a given destination.
    """
    prices = {
        "Rome": 150,
        "Paris": 200,
        "Barcelona": 180,
        "London": 220
    }
    return prices.get(destination, 120)


@mcp.tool()
def estimate_hotel(destination: str):
    """
    Estimate hotel price per night for a given destination.
    """
    prices = {
        "Rome": 80,
        "Paris": 120,
        "Barcelona": 100,
        "London": 150
    }
    return prices.get(destination, 70)