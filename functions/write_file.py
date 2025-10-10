import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites existing files or writes a file if it does not exist.  Creates parent dirs safely",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to write.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to a file",
            ),
        },
    ),
)



def write_file_content(working_dir, file_path, content):
    abs_working_dir = os.path.abspath(working_dir)
    abs_file_path = os.path.join(abs_working_dir, file_path)

    if not abs_file_path.startswith(abs_working_dir):
        return f'Cannot write: "{file_path}" as it is outside the permitted working directory "{working_dir}"'
    
    parent_dir = os.path.dirname(abs_file_path)

    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f'Could not create parent dir: {parent_dir}": {e}'

    try: 
        with open(abs_file_path, 'w') as file:
            file.write(content)

        return f'Successfully wrote to file: {abs_file_path} ({len(content)} characters)'
    except Exception as e:
        return f'Failed to writeto file: {abs_file_path}": {e}'
    



