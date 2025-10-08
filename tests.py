from functions import run_python_file
from functions.get_files_info import get_files_info

from functions.get_file_content import get_file_content
from functions.write_file import write_file_content
from functions.run_python_file import run_python_file

def main():
    working_directory = "calculator"

    # print(write_file_content(working_directory, "pkg/morelorem.txt", "Hello, world!"))
    # print(write_file_content(working_directory, "pkg2/morelorem.txt", "this dir does not exist"))
    # print(write_file_content(working_directory, "/tmp/temp.txt", "this should not be allowed"))

    print(run_python_file(working_directory, "main.py", ["3 + 5"]))
    # print(run_python_file(working_directory, "tests.py"))



if __name__ == "__main__":
    main()