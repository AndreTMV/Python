ones = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

tens_ones = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: ones[4] + 'teen',
    15: 'fifteen',
    16: ones[6] + 'teen',
    17: ones[7] + 'teen',
    18: ones[8] + 'een',
    19: ones[9] + 'teen',
}

tens = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}


def number_to_words(number: int) -> str:
    """TODO: Docstring for number_to_words.

                    :number: any number below one hundred
                    :returns: the number in word form (variable words)

                    """
    words: str
    if number < 10:
        return ones[number]
    if 10 <= number <= 19:
        return tens_ones[number]
    if 20 <= number <= 99:
        if number % 10 == 0:
            return tens[number]
        else:
            words = tens[(number // 10) * 10] + ones[number % 10]
            return words


def number_to_hundred(number: int) -> str:
    """TODO: Docstring for number_to_hundred.

                    :number: any number greater than 100 and below 1000
                    :returns: that number in word form (variable words)

                    """
    words: str
    if number == 1000:
        return 'onethousand'
    if number % 100 == 0:
        return ones[number // 100] + 'hundred'
    hundred_place: str = ones[number // 100] + 'hundred'
    decimal_place: str = number_to_words((number % 100))
    words = hundred_place + 'and' + decimal_place
    return words


def main():
    words: str
    total: int = 0
    for number in range(1, 1001):
        if number < 100:
            words = number_to_words(number)
            print(words)
            total += len(words)
        else:
            words = number_to_hundred(number)
            print(words)
            total += len(words)
    print(total)


if __name__ == "__main__":
    main()
