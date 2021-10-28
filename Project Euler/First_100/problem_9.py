import math


def pythagorean_triplet(expected_answer):
    """TODO: Docstring for pythagorean_triplet.

                    :arg1: the expected_answer from (a + b + c) if (a²+b²=c²)
                    :returns: product of abc if the expected_answer is the one

                    """
    for side_a in range(1, expected_answer//2):
        for side_b in range(1, expected_answer//2):
            for side_c in range(1, expected_answer//2):
                if side_a ** 2 + side_b ** 2 == side_c ** 2:
                    if side_a + side_b + side_c == expected_answer:
                        return side_a * side_b * side_c


def pythagorean_triplet_refactor(expected_answer: int) -> int:
    a: int = 0
    b: int = 0
    c: int = 0
    d: int = 0
    n: int = 0
    answer: int = expected_answer
    factor: int = 0
    reduced: int = 0
    limit: int = math.ceil(math.sqrt(expected_answer))
    expected_answer //= 2
    for number in range(2, limit):
        if expected_answer % number == 0:
            reduced = expected_answer // 2
            while reduced % 2 == 0:
                reduced //= 2
        if number % 2 == 1:
            factor = number + 2
        else:
            factor = number + 1
        while (factor < (2*number)) and factor <= limit:
            if (reduced % factor == 0) and (math.gcd(factor, number) == 1):
                d = expected_answer // (factor * number)
                n = factor - number
                a = d * (number * number - n * n)
                b = 2 * number * n * d
                c = d * (number * number + n * n)
                if a + b + c == answer:
                    return a * b * c
            factor += 2


print(pythagorean_triplet_refactor(1000))
