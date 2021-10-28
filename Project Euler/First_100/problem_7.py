import time
start_time = time.time()


def is_prime(number: int):
    """TODO: Docstring for is_prime.

                    :arg1: number
                    :returns: true if the number is prime

                    """
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def the_nth_prime(limit: int):
    """TODO: Docstring for the_nth_prime.

                    :arg1: limit
                    :returns: returns the prime number in limit position

                    """
    i: int = 1
    number: int = 2
    while i < limit:
        number = number + 1
        if(is_prime_refactor(number)):
            i = i + 1
    return number


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


print(f'{the_nth_prime(10001)} time:{time.time()-start_time}')
