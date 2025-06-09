# main.py

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    # Check for CLI argument
    if len(sys.argv) < 2:
        print("Error: Please provide a prompt as a command-line argument.")
        sys.exit(1)

    user_prompt = " ".join(sys.argv[1:])

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Environment variable GEMINI_API_KEY is not set")

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    print(response.text)

    usage = response.usage_metadata
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")

if __name__ == "__main__":
    main()
