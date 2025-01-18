def call_groq_api(prompt):
    try:
        data = {
            "input": prompt,       # Replace 'prompt' with the correct property
            "max_tokens": 100,     # Adjust as needed
            "stop": ["\n"]         # Optional, based on the API requirements
        }
        response = requests.post(GROQ_API_URL, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API call failed: {e}"}
