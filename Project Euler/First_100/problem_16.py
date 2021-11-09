def power_of_sum(base: int, exponent: int) -> int:
    """TODO: Docstring for power_of_sum.

                    :arg1: exponent, base
                    :returns: the sum of the numbers of base^exponent

                    """
    suma: int = 0
    for number in str(base**exponent):
        suma += int(number)
    return suma


print(power_of_sum(2, 1000))
