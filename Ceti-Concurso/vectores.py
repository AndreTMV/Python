def llenar_lista(size:int) -> list:
    """TODO: Docstring for llenar_lista.

                    :size: tamaño de la lista
                    :returns: TODO

                    """

    array:list = list(int(size) for size in input().strip().split())[:size]
    return array

def main() -> None:
    total:int = 0
    N:int = int(input())
    vector1 = llenar_lista(N)
    vector2 = llenar_lista(N)
    for index in range(N):
        total += vector1[index] * vector2[index]
    print(total)

if __name__ == "__main__":
    main()
