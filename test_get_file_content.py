from functions.get_file_content import get_file_content

def main():
    res1 = get_file_content("calculator", "main.py")
    print(f"Result for 'main.py' file:\n{res1}")
    res2 = get_file_content("calculator", "pkg/calculator.py")
    print(f"Result for 'pkg/calculator.py' file:\n{res2}")
    res3 = get_file_content("calculator", "/bin/cat")
    print(f"Result for '/bin/cat' directory:\n{res3}")
    res4 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"Result for 'pkg/does_not_exist.py' file:\n{res4}")

main()