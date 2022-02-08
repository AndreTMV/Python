def suma_fila(N: int) -> int:
    return 2 ** N


def suma_filas(T1: int, T2: int) -> int:
    total: int = 0
    for iteracion in range(T1, T2+1):
        total += suma_fila(iteracion)
    return total


def main() -> None:
    casos: int = int(input())
    for iteracion in range(casos):
        T1: int
        T2: int
        T1, T2 = map(int, input().split())
        print(suma_filas(T1, T2))


if __name__ == "__main__":
    main()
