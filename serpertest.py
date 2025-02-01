import requests

# Replace with your Serper Dev API key
SERPER_API_KEY = "438f44e29ac3aa83c0d6e6c7c0383adb0487c406"


# Endpoint for Serper API
url = "https://google.serper.dev/search"

# Example query to test the API
query = {
    "q": "What is the capital of France?"
}

# Set up headers with the API key
headers = {
    "X-API-KEY": SERPER_API_KEY
}

# Send a POST request to the Serper API
response = requests.post(url, headers=headers, json=query)

# Check the status and print the response
if response.status_code == 200:
    print("API Key is valid. Here's the response:")
    print(response.json())
else:
    print(f"API Key is invalid or there is an error. Status Code: {response.status_code}")
    print(response.text)