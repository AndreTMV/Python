def sum_of_squares_and_square_of_sums(limit):
    """TODO: Docstring for sum_of_squares_and_square_of_sums.

                    :arg1: limit
                    :returns: the substraction between the sum of the squares and the square of the sum for number from 1 to limit

                    """
    sum_of_squares = 0
    square_of_the_sum = sum_of_numbers = 0
    for number in range(0, limit + 1):
        sum_of_squares = sum_of_squares + (number ** 2)

    for number in range(0, limit + 1):
        sum_of_numbers = sum_of_numbers + number
    square_of_the_sum = sum_of_numbers ** 2
    return square_of_the_sum - sum_of_squares


def sum_of_squares(limit: int) -> float:
    """TODO: Docstring for sum_of_squares_.

                    :arg1: TODO
                    :returns: TODO

                    """
    return (int)(((2*limit)+1)*(limit+1))*(limit/6)


def square_of_sum(limit: int) -> float:
    return (int)((limit*(limit+1))/2) * ((limit*(limit+1))/2)


print(square_of_sum(100)-sum_of_squares(100))
