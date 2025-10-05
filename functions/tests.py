from get_file_content import get_file_content


def test_not_a_file():
    assert get_file_content("calculator", "pkg") == "Cannot read: \"pkg\" as it is not a file"

# def test_not_in_working_directory():
#     assert get_file_content("calculator", "../tests.py") == "Cannot read: \"../tests.py\" as it is outside the permitted working directory \"calculator\""

def main():
    test_not_a_file()


if __name__ == "__main__":
    main()