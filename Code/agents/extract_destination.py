from config.llm import client

def extract_destination_llm(user_input):

    prompt = f"""
    Extract the main travel destination from this request:

    {user_input}

    Return only the city or country name.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()