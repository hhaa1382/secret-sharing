from numpy import random


class MakeFunction:
    def __init__(self, S, t, n, p):
        self.p = p
        self.S = S
        self.t = t
        self.n = n

        self.func = [(self.S, 0)]

    def randomGenerator(self):
        return random.randint(1, self.p)

    def generateFunction(self):
        for i in range(1, self.t+1):
            num = self.randomGenerator()
            self.func.append((num, i))

    def getShares(self):
        values = []
        for x in range(self.n):
            temp = 0
            for val in self.func:
                temp += val[0]*(pow(x+1, val[1]))
            values.append(temp)
        return values

