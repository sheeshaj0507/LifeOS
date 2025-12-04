import os
import truststore
from openai import OpenAI
from dotenv import load_dotenv

# Inject system trust store to fix SSL issues
truststore.inject_into_ssl()

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY not found in .env file.")
    print("Please add your API key to the .env file.")
    exit(1)

client = OpenAI(api_key=api_key)

def test_model():
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Say hello from LifeOS!"}
            ]
        )
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys
    print(sys.path)
    test_model()
