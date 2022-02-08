def llenar_lista(size:int) -> list:
    """TODO: Docstring for llenar_lista.

                    :size: tamaño de la lista
                    :returns: TODO

                    """

    array:list = list(int(size) for size in input().strip().split())[:size]
    return array

def main() -> None:
    N:int = int(input())
    si:bool = True
    vector1 = llenar_lista(N)
    vector2 = llenar_lista(N)
    for index in range(N):
        if vector1[index] > vector2[index]:
            si = True
        else:
            si = False
            break
    if si:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
