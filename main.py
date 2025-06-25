import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions


def main():
    # Check for required arguments
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('Usage: python main.py "<prompt>" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    # Create client
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Generate content
    user_prompt = " ".join(args)
    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    model_name = "gemini-2.0-flash-001"

    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        )
    )

    metadata = response.usage_metadata

    if verbose:
        print(f"Prompt tokens: {metadata.prompt_token_count}")
        print(f"Response tokens: {metadata.candidates_token_count}")

    if not response.function_calls:
        print(f"Response:\n{response.text}")

    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")


if __name__ == "__main__":
    main()
