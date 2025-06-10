from functions.write_file import write_file


def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Test 1 - Overwrite 'lorem.txt':")
    print(result)
    print()

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Test 2 - Create new file in subdirectory:")
    print(result)
    print()

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Test 3 - Write outside working directory (should fail):")
    print(result)
    print()


if __name__ == "__main__":
    test()
