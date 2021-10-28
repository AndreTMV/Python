import time
start_time = time.time()


def fibonacci(limit: int) -> int:
    """TODO: Docstring for fibonacci.

                    :arg1: limit
                    :returns: the sum of all even terms before limit

                    """
    total: int
    third: int
    first: int
    second: int
    total = third = 0
    first = second = 1
    while third < limit:
        third = first + second
        if third % 2 == 0:
            total = total + third
        first = second
        second = third
    print(f"{first}, {second}, {third}")
    return total

# Refactor function


def fibonacci_refactor(limit: int) -> int:
    first: int
    second: int
    first = second = 1
    total: int = 0
    third: int = first + second
    while third < limit:
        total = total + third
        first = second + third
        second = third + first
        third = first + second
    return total


print(f"{fibonacci_refactor(4000000)} time: {time.time()-start_time}")
