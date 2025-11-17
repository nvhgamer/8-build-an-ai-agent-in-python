from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
    # result = get_files_info("calculator", ".")
    # print("Result for current directory:")
    # print(result)
    # print("")

    # result = get_files_info("calculator", "pkg")
    # print("Result for 'pkg' directory:")
    # print(result)

    # result = get_files_info("calculator", "/bin")
    # print("Result for '/bin' directory:")
    # print(result)

    # result = get_files_info("calculator", "../")
    # print("Result for '../' directory:")
    # print(result)

    # result = get_file_content("calculator", "lorem.txt")
    # print("Result for 'lorem.txt' file content:")
    # print(result)

    # result = get_file_content("calculator", "main.py")
    # print("Result for 'main.py' file content:")
    # print(result)

    # result = get_file_content("calculator", "pkg/calculator.py")
    # print("Result for 'pkg/calculator.py' file content:")
    # print(result)

    # result = get_file_content("calculator", "/bin/cat")
    # print("Result for '/bin/cat' file content:")
    # print(result)

    # result = get_file_content("calculator", "pkg/does_not_exist.py")
    # print("Result for 'pkg/does_not_exist.py' file content:")
    # print(result)

    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # print("Result for 'lorem.txt' write:")
    # print(result)

    # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print("Result for 'pkg/morelorem.txt' write:")
    # print(result)

    # result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    # print("Result for '/tmp/temp.txt' write:")
    # print(result)

    result = run_python_file("calculator", "main.py")
    print("Result for 'main.py' (no args):")
    print(result)
    print()

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for 'main.py' (with args ['3 + 5']):")
    print(result)
    print()

    result = run_python_file("calculator", "tests.py")
    print("Result for 'tests.py':")
    print(result)
    print()

    result = run_python_file("calculator", "../main.py")
    print("Result for '../main.py':")
    print(result)
    print()

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for 'nonexistent.py':")
    print(result)
    print()

    result = run_python_file("calculator", "lorem.txt")
    print("Result for 'lorem.txt':")
    print(result)
    print()

if __name__ == "__main__":
    test()
