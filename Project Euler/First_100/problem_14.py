global CACHE_SIZE
CACHE_SIZE = 1_000_000
cache = [0] * CACHE_SIZE


def hailstone(number: int) -> int:
    if number & 1:
        return 3*number + 1
    else:
        return number >> 1


class Superlatives:
    __max_state: int
    __min_state: int
    __max_val: int
    __min_val: int
    __valid: bool

    def __init__(self) -> None:
        """Constructor for __init"""
        self.__valid = False

    def add_sate(self, state,  val) -> None:
        if (self.__valid):
            if (val > self.__max_val):
                self.__max_val = val
                self.__max_state = state
            elif (val < self.__min_val):
                self.__min_val = val
                self.__min_state = state

        else:
            self.__min_val = val
            self.__max_val = val
            self.__min_state = state
            self.__max_state = state
            self.__valid = True

    def max_val(self) -> int:
        return self.__max_val

    def min_val(self) -> int:
        return self.__min_val

    def max_state(self) -> int:
        return self.__max_state

    def min_state(self) -> int:
        return self.__min_state

    def is_valid(self) -> int:
        return self.__valid


def find_depth(number: int) -> int:
    d: int = 0
    if number == 1:
        return 0
    if number < CACHE_SIZE and cache[number]:
        return cache[number]
    d = find_depth(hailstone(number)) + 1
    if number < CACHE_SIZE:
        cache[number] = d
    return d


def main():
    N: int = 1000000
    supe = Superlatives()
    i: int
    for i in range(2, N):
        supe.add_sate(i, find_depth(i))
    print(f"{supe.max_val()} has a chain of length {supe.max_state()}")


if __name__ == '__main__':
    main()
