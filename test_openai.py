import openai
import os
# Load API key from environment variable
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

# Test GPT model
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Change model as needed (e.g., "gpt-4" or "gpt-3.5-turbo")
    messages=[{"role": "user", "content": "Tell me a fun fact about AI."}],
    temperature=0.7
)

# Print response
print(response.choices[0].message.content)