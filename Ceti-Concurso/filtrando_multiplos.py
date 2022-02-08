def llenar_lista(size:int) -> list:
    """TODO: Docstring for llenar_lista.

                    :size: tamaño de la lista
                    :returns: TODO

                    """

    array:list = list(int(size) for size in input().strip().split())[:size]
    return array

def multiplo(number:int, multiple:int) -> None:
    if number % multiple == 0:
        print(number, end = ' ')
    else:
        print('X', end = ' ')

def main() -> None:
    N:int = int(input())
    array:list = llenar_lista(N)
    multiplo:int = int(input())
    for element in array:
        if element % multiplo == 0:
            print(element, end = ' ')
        else:
            print('X', end = ' ')
    print()

if __name__ == "__main__":
    main()
