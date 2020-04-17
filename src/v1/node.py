class Node:
    def __init__(self):
        """Constructor"""
        self.value = None
        self.next = None

    def __str__(self):
        return "Node [value = {}, has_next = {}]".format(self.value, self.__has_next())

    def __has_next(self):
        return self.next is not None
