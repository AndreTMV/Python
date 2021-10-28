import pdb
import re
from operator import mul
from functools import reduce


def primes_3_5(limit):
    """TODO: Docstring for primes_3_5.

                    :arg1: limit
                    :returns: the sum of all the multiples of 3 and 5 below the limit

                    """
    total = 0
    for number in range(0, limit):
        if (number % 3 == 0) or (number % 5 == 0):
            print(number, "\n")
            total += number
    return total


def fibonacci(limit):
    """TODO: Docstring for fibonacci.

                    :arg1: limit
                    :returns: the sum of all even terms before limit

                    """
    total = third = 0
    first = second = 1
    while third < limit:
        third = first + second
        if third % 2 == 0:
            total = total + third
        first = second
        second = third
    print(f"{first}, {second}, {third}")
    return total


def largest_prime_number(number):
    """TODO: Docstring for largest_prime_number.

                    :arg1: number
                    :returns: the largest prime number of that number

                    """
    primes = []
    decomposer = 2
    while decomposer <= number:
        if number == 1 or number == 0:
            break
        elif number % decomposer == 0:
            number = number / decomposer
            primes.append(decomposer)
        else:
            decomposer = decomposer + 1
    return max(primes)


def reverse(number):
    """TODO: Docstring for reverse.

                    :arg1: number
                    :returns: the reverse of that number ex: 123 -> 321

                    """
    reverse_number = 0
    while number > 0:
        reverse_number = (reverse_number * 10) + (number % 10)
        number = number // 10
    return(reverse_number)


def largest_three_digit_palindromic():
    """TODO: Docstring for largest_three_digit_palindromic.

                    :arg1: nothing
                    :returns: the largest palindromic number of three digit

                    """
    test_number = largest_palindromic = 0
    for first_number in range(0, 1000):
        for second_number in range(0, 1000):
            test_number = first_number * second_number
            if(test_number == reverse(test_number)):
                if(test_number > largest_palindromic):
                    largest_palindromic = test_number

    return largest_palindromic


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


def is_prime(number):
    """TODO: Docstring for is_prime.

                    :arg1: number
                    :returns: true if the number is prime

                    """
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def the_nth_prime(limit):
    """TODO: Docstring for the_nth_prime.

                    :arg1: limit
                    :returns: returns the prime number in limit position

                    """
    i = 1
    number = 2
    while i < limit:
        number = number + 1
        if(is_prime(number)):
            i = i + 1
    return number


def from_integer_to_a_list_of_all_its_digits():
    """TODO: Docstring for from_integer_to_a_list_of_all_its_digits

                    :arg1: number
                    :returns: comma separated value

                    """
    number = """
        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450
    """
    number = number.replace(" ", "").replace("\n", "")
    integers = [int(i) for i in str(number)]
    return integers


def largest_thirteen_product_sum(integers):
    lenght = len(integers)
    substring_l = 13
    answer = 0
    for index in range(lenght - substring_l + 1):
        subset = integers[index:index+substring_l]
        product = reduce(mul, subset, 1)
        answer = max(product, answer)
    return answer


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


def sum_of_primes_under(limit):
    """TODO: Docstring for sum_of_primes_under.

                    :arg1: limit
                    :returns: sum of all the primes before limit

                    """
    primes = [number for number in range(2, limit) if(is_prime(number))]
    return sum(primes)


def largest_product_in_grid(grid):
    largest_product = 0
    max_off_set = 4
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            cell = grid[row][column]
            product = 0
            # Vertical
            product = cell
            for i in range(1, max_off_set):
                try:
                    grid[row] and grid[row][column + i]
                except:
                    break
                else:
                    product = product * grid[row][column + i]

            if product > largest_product:
                largest_product = product

            # Horizontal
            product = cell
            for i in range(1, max_off_set):
                try:
                    grid[row + i] and grid[row + i][column]
                except:
                    break
                else:
                    product = product * grid[row + i][column]

            if product > largest_product:
                largest_product = product

            # Diagonal arriba a abajo
            product = cell
            for i in range(1, max_off_set):
                try:
                    grid[row + i] and grid[row + i][column + i]
                except:
                    break
                else:
                    product = product * grid[row + i][column + i]

            if product > largest_product:
                largest_product = product

            # Diagonal abajo a arriba
            product = cell
            for i in range(1, max_off_set):
                try:
                    grid[row - i] and grid[row - i][column + i]
                    if (row-i) < 0:
                        raise IndexError
                except IndexError:
                    break
                else:
                    product = product * grid[row - i][column + i]

            if product > largest_product:
                largest_product = product
    return largest_product


grid = [
    [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71,
        40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92,
        36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38,
        40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78,
        78, 96, 83, 14, 88, 34, 89, 63, 72],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
    [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33,
        67, 46, 55, 12, 32, 63, 93, 53, 69],
    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62,
        99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
]
