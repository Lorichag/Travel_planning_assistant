from config.llm import client

def run_verification(all_data):

    prompt = f"""
    Verify and improve this travel plan:

    {all_data}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content