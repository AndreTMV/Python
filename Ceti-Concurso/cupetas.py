def llenar_lista(size:int) -> list:
    """TODO: Docstring for llenar_lista.

                    :size: tamaño de la lista
                    :returns: TODO

                    """

    array:list = list(int(size) for size in input().strip().split())[:size]
    return array

def main() -> None:
    N:int = 0
    M:int = 0
    N, M = map(int, input().split())
    lista = llenar_lista(N)
    frecuencia = {}
    for element in range(1, M + 1):
        frecuencia[element] = 0
    for element in lista:
        if element in frecuencia:
            frecuencia[element] += 1;
        else:
            frecuencia[element] = 1
    for key, value in frecuencia.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
