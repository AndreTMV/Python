def reverse(number1: int, number2: int) -> int:
    """TODO: Docstring for reverse.

                    :arg1: number
                    :returns: the reverse of that number ex: 123 -> 321

                    """
    number: int = number1 * number2
    reverse_number: int = 0
    while number > 0:
        reverse_number = (reverse_number * 10) + (number % 10)
        number = number // 10
    return reverse_number


def is_palindrome(number1: int, number2: int) -> bool:
    """TODO: Docstring for is_prime.

                    :number1,number2: check if the product of this factors is a palindrome
                    :returns: true if it is a  palindrome

                    """
    return reverse(number1, number2) == number1 * number2


def largest_three_digit_palindromic():
    """TODO: Docstring for largest_three_digit_palindromic.

                    :arg1: nothing
                    :returns: the largest palindromic number of three digit

                    """
    test_number = largest_palindromic = 0
    for first_number in range(0, 1000):
        for second_number in range(0, 1000):
            if(test_number == reverse(first_number, second_number)):
                if(test_number > largest_palindromic):
                    largest_palindromic = test_number

    return largest_palindromic


def largest_three_digit_palindromic_refactor(limit: int) -> int:
    """TODO: Docstring for largest_three_digit_palindromic_refactor.

                    :arg1: TODO
                    :returns: TODO

                    """
    largest_palindromic: int = 0
    first_number: int = limit
    while first_number > 0:
        second_number: int = first_number
        while second_number > 0:
            if first_number*second_number <= largest_palindromic:
                break
            if(is_palindrome(first_number, second_number)):
                largest_palindromic = first_number*second_number
            second_number -= 1
        first_number -= 1

    return largest_palindromic


print(largest_three_digit_palindromic_refactor(1000))
