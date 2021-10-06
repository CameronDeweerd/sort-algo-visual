import random
import copy


class DataSet:

    def __init__(self, size=50, start="random"):
        self.values = [i+1 for i in range(size)]

        if start == "random":
            self.random_order()

        if start == "reverse":
            self.reverse_order()

        if start == "ordered":
            pass

    def reverse_order(self):
        self.values.reverse()

    def random_order(self):
        random.shuffle(self.values)

    def duplicate(self):
        return copy.deepcopy(self)
