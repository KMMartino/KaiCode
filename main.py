import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()


    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text = args.user_prompt)])]
    response = client.models.generate_content(
        model = "gemini-3-flash-preview", contents = messages)
    
    prompt_tokens = response.usage_metadata.prompt_token_count
    completion_tokens = response.usage_metadata.candidates_token_count

    if args.verbose:
        print(f"User prompt: {messages}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {completion_tokens}")

    print(response.text)








if __name__ == "__main__":
    main()
