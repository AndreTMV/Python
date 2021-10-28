def divisor_numbers(number: int) -> int:
    """TODO: Docstring for prime_numbers.

                    :arg1: a number
                    :returns: the number of divisors

                    """
    divisor: int = 2
    exponent: int = 0
    count: int = 1
    while number > 1:
        exponent = 0
        while number % divisor == 0:
            number //= divisor
            exponent += 1
        count *= (exponent + 1)
        divisor += 1
    return count


def first_triangle_number_greater_500() -> int:
    """TODO: Docstring for first_triangle_number_greater_500.

                    :arg1: nothing
                    :returns: the first triangle number with more than 500 divisors

                    """
    target_divisors: int = 500
    position: int = 0
    number_divisors: int = 0
    left_divisor: int = 1
    right_divisor: int = 0
    while True:
        position += 1
        if position + 1 & 1:
            right_divisor = divisor_numbers(position + 1)
        else:
            right_divisor = divisor_numbers((position + 1) // 2)
        number_divisors = left_divisor * right_divisor
        if number_divisors > target_divisors:
            return position * (position + 1) // 2
        left_divisor = right_divisor


print(first_triangle_number_greater_500())
