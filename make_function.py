from numpy import random


class MakeFunction:
    def __init__(self, S, t, n, p):
        self.p = p
        self.S = S
        self.t = t
        self.n = n

        self.func = [self.S]

    def randomGenerator(self):
        return random.rand(self.t)

    def generateFunction(self):
        num = self.randomGenerator()
        for i in range(1, self.t+1):
            self.func.append((num, i))


