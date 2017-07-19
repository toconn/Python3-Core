class AutoCounter:

    def __init__(self, start_value = 0):

        self.__next = start_value

    def next(self):

        next_value = self.__next
        self.__next += 1
        return next_value

class Counter:

    def __init__(self, start_value = 0):
        self.__count = 0

    def count(self):
        return self.__count

    def increment(self):
        self.__count += 1