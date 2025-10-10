import os

from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)

    abs_dir = os.path.abspath(os.path.join(abs_working_dir, directory))

    if not abs_dir.startswith(abs_working_dir):
        return f'Error: "{directory}" is not in the working directory "{working_directory}"'


    final_response = ""

    contents = os.listdir(abs_dir)
    for content in contents:
        content_path = os.path.join(abs_dir, content)
        is_dir = os.path.isdir(content_path)
        
        size = os.path.getsize(content_path)

        final_response += f"- {content}: file_size: {size} bytes, is_dir: {is_dir}\n"

        # print(f"Response: {final_response}")

    return final_response


