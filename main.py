import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import schema_get_files_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

from google.genai import types

from call_function import call_function



def main():

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    # api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    print("Hello from gemini-agent!")
    print("Args", sys.argv)
    
    if len(sys.argv) < 2: 
        exit("Usage: python main.py [--verbose] <prompt>", code=1)

    verbose_flag = False

    if len(sys.argv) == 3 and sys.argv[1] == "--verbose":
        verbose_flag = True
        print ("verbose mode on")

    prompt = sys.argv[2]

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Write to a file
- Get file content
- Run a python file

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
    


    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=prompt)]
        )
    ]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_write_file,
            schema_get_files_content,
            schema_run_python_file
        ]
    )

    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )

    
    # print(f"Prompt: {prompt}")

    response = client.models.generate_content(
        model = "gemini-2.0-flash-001", 
        contents=messages,
        config=config
        )

    if verbose_flag:
        print(f"User prompt: {prompt}")
        # print(f"System prompt: {system_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


    if response is None or response.usage_metadata is None:
        print("response is malformed:")
        exit(1)
    

    if response.function_calls:
        for function_call_part in response.function_calls:
            result = call_function(function_call_part, verbose_flag)
            # print(result)

    # print(response.text)

    

    
    


if __name__ == "__main__":
    main()
    # print(get_files_info("calculator", "pkg"))
    # print(get_files_info("calculator"))
