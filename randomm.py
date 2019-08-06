import numpy as np


class Randomm:
    test = 0

    def __init__(self):
        self.test = 0

    def ran(self, x, y):
        k = np.random.randint(x, y)
        return k

    def ranFloat(self,x, y):
        random_float_number = np.random.uniform(x, y)
        return random_float_number
