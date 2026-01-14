from logging import config
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
import LLM_config

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

    for _ in range(20):
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = messages,
            config = types.GenerateContentConfig(
                system_instruction=LLM_config.system_prompt, 
                tools=[LLM_config.available_functions]
            ),
        )

        prompt_tokens = response.usage_metadata.prompt_token_count
        completion_tokens = response.usage_metadata.candidates_token_count

        if args.verbose:
            print(f"User prompt: {messages}")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {completion_tokens}")


        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if response.function_calls != None:
            resultslist = []
            for call in response.function_calls:
                function_call_result = LLM_config.call_function(call)
                if not function_call_result.parts:
                    raise Exception(f"Error: function call {call} did not return: no parts(0)")
                if not function_call_result.parts[0].function_response:
                    raise Exception(f"Error: function call {call} did not return: no function_response(1)")
                if function_call_result.parts[0].function_response.response == None:
                    raise Exception(f"Error: function call {call} did not return: no response(2)")
                resultslist.append(function_call_result.parts[0])
                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
            messages.append(types.Content(role="user", parts=resultslist))

        else:
            print(response.text)
            return

    print("Agent exceeded iteration limit: exiting program with code 1")
    exit(1)


if __name__ == "__main__":
    main()
