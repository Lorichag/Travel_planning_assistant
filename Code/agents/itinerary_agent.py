from config.llm import client

def run_itinerary(research_output):

    prompt = f"""
    Create a day-by-day itinerary based on:

    {research_output}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content