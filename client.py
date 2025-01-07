import requests

def get_generated_text(api_token, model_name, prompt, max_length=50):
    """
    Function to get generated text from Hugging Face API.

    Parameters:
    - api_token: str, your Hugging Face API token.
    - model_name: str, name of the Hugging Face model (e.g., 'gpt2').
    - prompt: str, the input text to generate text from.
    - max_length: int, maximum length of the generated text.

    Returns:
    - str, generated text.
    """
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    data = {
        "inputs": prompt,
        "parameters": {
            "max_length": max_length
        }
    }

    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result[0]['generated_text']
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
