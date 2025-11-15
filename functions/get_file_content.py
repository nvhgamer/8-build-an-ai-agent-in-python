import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    # Get the absolute paths of the working directory and target file
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    # Ensure the target file is within the working directory
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # Check if the target file exists and is a file
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    # Read and return the content of the file
    try:
        with open(target_file, 'r') as f:
            # Read up to MAX_CHARS + 1 to get the contents of the file and also be able to check if it exceeds the limit
            content = f.read(MAX_CHARS + 1)

            # Truncate if necessary
            if len(content) > MAX_CHARS:
                truncated = content[:MAX_CHARS]
                trunc_note = f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return truncated + trunc_note

            # Otherwise, return full content as is
            return content
    except Exception as e:
        return f"Error reading file: {e}"