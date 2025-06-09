# main.py

import os
from dotenv import load_dotenv
from google import genai
import sys

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a prompt as a command-line argument.")
        sys.exit(1)
    prompt = " ".join(sys.argv[1:])

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Environment variable GEMINI_API_KEY is not set")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt
    )

    
    print(response.text)

    
    usage = response.usage_metadata
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")

if __name__ == "__main__":
    main()
