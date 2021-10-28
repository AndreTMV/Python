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
