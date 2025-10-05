import os

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

    return final_response


