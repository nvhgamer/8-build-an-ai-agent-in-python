import json

from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file import schema_write_file, write_file
from functions.run_python_file import schema_run_python_file, run_python_file
from config import WORKING_DIR

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)


def call_function(function_call_part, verbose=False):
    """
    Given a function_call_part from the model, parse its args, ensure working_directory
    is present, call the local function and return a types.Content built with
    Part.from_function_response(...) containing {"result": function_result} or an error dict.
    """

    function_name = function_call_part.name

    if verbose:
        print(f"Calling function: {function_name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")

    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    # If the function is not found, return an error response
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    # Add the working_directory to the function call arguments
    function_call_part.args["working_directory"] = WORKING_DIR

    # Get the function to call
    func = function_map.get(function_name)
    
    # Call the function with the provided arguments
    function_result = func(**function_call_part.args)

    # Wrap the function result in the required dict form for from_function_response
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )