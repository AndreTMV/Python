def main() -> None:
    a:int = 0
    b:int = 0
    c:int = 0
    a, b, c = map(int, input().split())
    if a < b:
        print(True, end = ' ')
    else:
        print(False, end =  ' ')
    if c > a:
        print(True, end =  ' ')
    else:
        print(False, end = ' ')
    if a == b:
        print(True, end = ' ')
    else:
        print(False, end =  ' ')
    if a != c:
        print(True, end = ' ')
    else:
        print(False, end =  ' ')
    if c <= b:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
