def llenar_lista(size: int):
    """TODO: Docstring for llenar_lista.

                    :size: tamaño de la lista
                    :returns: TODO

                    """

    array = (list(int(size) for size in input().strip().split())[:size])
    return array


def suma(lista) -> int:
    max_suma: int = lista[0]
    suma: int = max_suma
    for index in range(1, len(lista)):
        suma = max(lista[index] + suma, lista[index])
        max_suma = max(max_suma, suma)
    return max_suma


def main() -> None:
    size = int(input())
    array = (int(size) for size in input().strip().split())
    print(type(array))
    print(suma(array))


if __name__ == "__main__":
    main()
