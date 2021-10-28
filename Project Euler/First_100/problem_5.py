def smallest_positive_number(limit):
    """TODO: Docstring for smallest_positive_number.

                    :arg1: limit
                    :returns: returns the smallest_positive_number divisble by 1 to limit

                    """
    dividend = limit
    dividers = [divider for divider in range(1, limit + 1)]
    while True:
        if(all((dividend % divider == 0) for divider in dividers)):
            break
        else:
            dividend = dividend + 1
    return dividend
