import os

from config import MAX_CHARS

def get_file_content(working_dir, file_path):
    abs_working_dir = os.path.abspath(working_dir);
    abs_file_path = os.path.join(abs_working_dir, file_path)

    if not abs_file_path.startswith(abs_working_dir):
        return f'Cannot read: "{file_path}" as it is outside the permitted working directory "{working_dir}"'

    if not os.path.isfile(abs_file_path):
        return f'Cannot read: "{file_path}" as it is not a file'

    file_content_string = ""

    try:

        with open(abs_file_path, 'r') as file:
            file_content_string = file.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += f"\n... File {file_path} (truncated at {MAX_CHARS} characters)"

    except Exception as e:
        return f"Exception reading file {file_path}: {e}"

    return file_content_string