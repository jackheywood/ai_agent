from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def test_get_files_info():
    print("┌────────────────────────┐")
    print("| Testing get_files_info |")
    print("└────────────────────────┘\n")

    result = get_files_info("calculator", ".")
    print_result(result, "current directory")

    result = get_files_info("calculator", "pkg")
    print_result(result, "'pkg' directory")

    result = get_files_info("calculator", "/bin")
    print_result(result, "'/bin' directory")

    result = get_files_info("calculator", "../")
    print_result(result, "'../' directory")


def test_get_file_content():
    print("┌──────────────────────────┐")
    print("| Testing get_file_content |")
    print("└──────────────────────────┘\n")

    result = get_file_content("calculator", "lorem.txt")
    print_result(result, "'lorem.txt' file")

    result = get_file_content("calculator", "main.py")
    print_result(result, "'main.py' file")

    result = get_file_content("calculator", "pkg/calculator.py")
    print_result(result, "'pkg/calculator.py' file")

    result = get_file_content("calculator", "/bin/cat")
    print_result(result, "'/bin/cat' file")


def print_result(result, message):
    print(f"Result for {message}:")
    print(result)
    print()


if __name__ == "__main__":
    test_get_files_info()
    test_get_file_content()
