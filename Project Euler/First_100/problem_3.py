import math


def largest_prime_number(number: int) -> int:
    """TODO: Docstring for largest_prime_number.

                    :arg1: number
                    :returns: the largest prime number of that number

                    """
    primes: list = []
    decomposer: int = 2
    while decomposer <= number:
        if number == 1 or number == 0:
            break
        elif number % decomposer == 0:
            number = number // decomposer
            primes.append(decomposer)
        else:
            decomposer = decomposer + 1
    return max(primes)


# Refactored function
def largest_prime(number: int) -> int:
    """TODO: Docstring for largest_prime.

                    :number: a number
                    :returns: the largest prime of that number

                    """
    last_Factor: int = 0
    if number % 2 == 0:
        last_Factor = 2
        number = number // 2
        while number % 2 == 0:
            number = number // 2
    else:
        lastFactor = 1
    factor: int = 3
    maxFactor: int = math.floor(math.sqrt(number))
    while number > 1 and factor <= maxFactor:
        if number % factor == 0:
            number = number // factor
            last_Factor = factor
            while number % factor == 0:
                number = number // factor
            maxFactor = math.floor(math.sqrt(number))
        factor = factor + 2
    if number == 1:
        return last_Factor
    else:
        return number


print(largest_prime(600851475143))
