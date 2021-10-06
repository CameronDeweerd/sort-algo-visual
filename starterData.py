import random


class DataSet:

    def __init__(self, size=50, start="random"):
        self.values = [i+1 for i in range(size)]

        if start == "random":
            self.random_order()

        if start == "reverse":
            self.reverse_order()

        if start == "ordered":
            pass

        print(self.values)

    def reverse_order(self):
        reversed(self.values)

    def random_order(self):
        random.shuffle(self.values)
