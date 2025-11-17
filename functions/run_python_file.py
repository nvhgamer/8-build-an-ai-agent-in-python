import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    # Get the absolute paths of the working directory and target file
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    # Ensure the target file is within the working directory
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    # Check if the target file exists and is a file
    if not os.path.isfile(target_file):
        return f'Error: File "{file_path}" not found.'
    
    # Check if the file ends with .py
    if not target_file.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:

        cmd = ["python", target_file] + list(args)
        completed_process = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=abs_working_dir,
            timeout=30,
        )

        stdout = completed_process.stdout or ""
        stderr = completed_process.stderr or ""

        if not stdout and not stderr:
            return "No output produced."

        output = f"STDOUT: {stdout}\nSTDERR: {stderr}".rstrip()

        if completed_process.returncode != 0:
            output += f"\nProcess exited with code {completed_process.returncode}"

        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"