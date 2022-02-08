def llenar_lista(elementos: list[list]) -> None:
    elemento: int = 0
    for row in range(1, len(elementos)):
        valores = map(int, input().split())
        for col in range(1, row):
            if elemento % 2 == 0:
                elementos[row][col] = elemento


def mejor_camino(elementos: list[list], N: int) -> int:
    camino: int = 0
    for row in range(N - 1, 0, -1):
        for col in range(0, row + 1):
            camino = max(elementos[row + 1][col], elementos[row + 1][col + 1])
            elementos[row][col] += camino
    return elementos[1][1]


def main() -> None:
    N: int = int(input())
    elementos: list[list] = [[0 for i in range(N)] for j in range(N)]
    llenar_lista(elementos)
    print(mejor_camino(elementos, N)

if __name__ == "__main__":
    main()
