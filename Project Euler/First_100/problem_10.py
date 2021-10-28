def is_prime(number):
    """TODO: Docstring for is_prime.

                    :arg1: number
                    :returns: true if the number is prime

                    """
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def sum_of_primes_under(limit):
    """TODO: Docstring for sum_of_primes_under.

                    :arg1: limit
                    :returns: sum of all the primes before limit

                    """
    primes = [number for number in range(2, limit) if(is_prime(number))]
    return sum(primes)


def is_prime_refactor(number: int):
    if number == 1:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    elif number < 9:
        return True
    elif number % 3 == 0:
        return False
    else:
        limit: int = int(number ** .5)
        factor: int = 5
        while factor <= limit:
            if number % factor == 0:
                return False
            if number % (factor + 2) == 0:
                return False
            factor = factor + 6
    return True


def sum_of_primes(limit: int) -> int:
    total_sum: int = 0
    for number in range(limit):
        if is_prime_refactor(number):
            total_sum += number
    return total_sum


print(sum_of_primes(2_000_000))
