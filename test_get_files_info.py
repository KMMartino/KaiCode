from functions.get_files_info import get_files_info

def main():
    res1 = get_files_info("calculator", ".")
    print(f"Result for current directory:\n{res1}")
    res2 = get_files_info("calculator", "pkg")
    print(f"Result for 'pkg' directory:\n{res2}")
    res3 = get_files_info("calculator", "/bin")
    print(f"Result for '/bin' directory:\n{res3}")
    res4 = get_files_info("calculator", "../")
    print(f"Result for '../' directory:\n{res4}")

main()