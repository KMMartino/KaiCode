from functions.write_file import write_file

def main():
    res1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Result for 'main.py' file:\n{res1}")
    res2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Result for 'pkg/calculator.py' file:\n{res2}")
    res3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Result for '/bin/cat' directory:\n{res3}")
main()