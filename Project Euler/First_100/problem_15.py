def count_routes(gridSize: int) -> int:
    paths: int = 1
    for number in range(0, gridSize):
        paths *= (2*gridSize) - number
        paths //= number + 1
    return paths


def main():
    return count_routes(20)


if __name__ == "__main__":
    print(main())
