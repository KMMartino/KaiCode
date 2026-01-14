from functions.run_python_file import run_python_file

def main():
    res1 = run_python_file("calculator", "main.py")
    print(f"Result for 'main.py' file:\n{res1}")
    res2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"Result for 'main.py' file with arguments:\n{res2}")
    res3 = run_python_file("calculator", "tests.py")
    print(f"Result for 'tests.py' file:\n{res3}")
    res4 = run_python_file("calculator", "../main.py")
    print(f"Result for '../main.py' file:\n{res4}")
    res5 = run_python_file("calculator", "nonexistent.py")
    print(f"Result for 'nonexistent.py' file:\n{res5}")
    res6 = run_python_file("calculator", "lorem.txt")
    print(f"Result for 'lorem.txt' file:\n{res6}")
main()