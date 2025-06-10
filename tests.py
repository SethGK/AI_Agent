from functions.run_python import run_python_file

def test():
    result = run_python_file("calculator", "main.py")
    print("Test 1 - Run 'main.py':")
    print(result)
    print()

    result = run_python_file("calculator", "tests.py")
    print("Test 2 - Run 'tests.py':")
    print(result)
    print()

    result = run_python_file("calculator", "../main.py")
    print("Test 3 - Attempt to run file outside working dir (should fail):")
    print(result)
    print()

    result = run_python_file("calculator", "nonexistent.py")
    print("Test 4 - Attempt to run non-existent file (should fail):")
    print(result)
    print()


if __name__ == "__main__":
    test()
