import os
from openai import OpenAI

# Initialize the client (it will look for your OPENAI_API_KEY environment variable)
client = OpenAI()

def test_connection():
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful engineering assistant."},
                {"role": "user", "content": "Say 'AI Core is online' and verify you are ready."}
            ]
        )
        print("Response from model:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error connecting: {e}")

if __name__ == "__main__":
    test_connection()