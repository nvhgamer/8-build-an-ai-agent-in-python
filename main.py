import os
import sys
from urllib import response

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    load_dotenv()

    args = sys.argv[1:]

    verbose = False

    non_flag_tokens = []

    # Parse command-line arguments by looping through sys.argv
    for a in args:
        # Check if there is a "--verbose" flag
        if a == "--verbose":
            verbose = True
        # Check for other flags starting with "--"
        elif a.startswith("--"):
            # ignore unknown flags for now
            continue
        # Otherwise, treat it as part of the prompt
        else:
            non_flag_tokens.append(a)

    # Ensure that there is at least one non-flag argument (the prompt)
    if not non_flag_tokens:
        print("Error: No prompt provided. Usage: uv run main.py \"<prompt>\" [--verbose]")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(non_flag_tokens)

    if verbose:
        print(f'User prompt: {user_prompt}')

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose=False):    
    response: types.GenerateContentResponse | None = None
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        ),
    )

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        return response.text

    function_responses = []
    
    for function_call_part in response.function_calls:
        # Call the function
        function_call_result = call_function(function_call_part, verbose)

        # Check if the function call result is valid
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("Function call did not return any result.")

        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

if __name__ == "__main__":
    main()
