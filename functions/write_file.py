import os

from google.genai import types

def write_file(working_directory, file_path, content):
    # Get the absolute paths of the working directory and target file
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    # Ensure the target file is within the working directory
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        # Create directories if they do not exist
        if not os.path.exists(os.path.dirname(target_file)):
            os.makedirs(os.path.dirname(target_file))

        # Write the content to the file
        with open(target_file, 'w') as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing file: {e}"
    
# Define the function schema for use with the AI model
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write into the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)