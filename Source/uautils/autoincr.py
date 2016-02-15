class AutoIncr:

    def __init__(self, start_value = 0):

        self.__next = start_value

    def next(self):

        next_value = self.__next
        self.__next += 1
        return next_value
