def primes_3_5(limit: int) -> int:
    """TODO: Docstring for primes_3_5.

                    :arg1: limit
                    :returns: the sum of all the multiples of 3 and 5 below the limit

                    """
    total: int = 0
    for number in range(0, limit):
        if (number % 3 == 0) or (number % 5 == 0):
            print(number, "\n")
            total += number
    return total

# Refactoring the function


def sum_divisible_by(limit: int, number: int) -> int:
    target: int = limit//number
    # Sum of the number to x = (x*(x+1))/2
    return number*(target*(target+1)) // 2


print(sum_divisible_by(999, 3)+sum_divisible_by(999, 5) - sum_divisible_by(999, 15))
