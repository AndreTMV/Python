def tabla_de_x(limit: int) -> None:
    lista = [x for x in range(1, limit)]
    for number in lista:
        print(f"{limit} x {number} = {number*limit}")


tabla_de_x(7)
