def main() -> None:
    x:float = 0
    y:float = 0
    z:float = 0
    x, y, z = map(float, input().split())
    print(round(((2 * x + y) / z) * ((y ** 3) - z) / (((x + 2 * y + 3 * z) / (z - 2 * y - 3 * x)) + (x ** 2) + (z ** 2)),6))

if __name__ == "__main__":
    main()
