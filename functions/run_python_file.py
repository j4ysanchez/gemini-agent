import os
import subprocess

from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file with the python interpreter.  Accepts additional arugments as an optional array",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array of STRING arguments to run with the python file",
                items=types.Schema(type=types.Type.STRING)
            ),
        },
    ),
)



def run_python_file(working_dir, file_path: str, args=None):

    abs_working_dir = os.path.abspath(working_dir)
    abs_file_path = os.path.join(abs_working_dir, file_path)

    if not abs_file_path.startswith(abs_working_dir):
        return f'Cannot run: "{file_path}" as it is outside the permitted working directory "{working_dir}"'

    if not os.path.isfile(abs_file_path):
        return f'Cannot run: "{file_path}" as it is not a file'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a python file'

    final_string = ""

    try:
        final_args = ["python3", file_path]
        if args:
            final_args.extend(args)


        # final_string =  f"""
        #         STDOUT: {output.stdout}
        #         STDERR: {output.stderr}
        #     """
        
        completed = subprocess.run(
            final_args,
            cwd=abs_working_dir,
            timeout=30,
            capture_output=True,
            text=True,
        )

        stdout = completed.stdout or ""
        stderr = completed.stderr or ""

 # if output.stdout == "" and output.stderr == "No output produced. \n":
        #     final_string = "No output provided \n"
    

        # if output.returncode != 0:
        #     final_string += f"Process exited with code {output.returncode}"

        if completed.returncode != 0:
            return f"STDOUT:\n{stdout}\nSTDERR:\n{stderr}\nProcess exited with code {completed.returncode}"

        return stdout if stdout else (stderr if stderr else "No output produced.\n")

    except Exception as e:
        return f'Error: executing Python file: {e}'

