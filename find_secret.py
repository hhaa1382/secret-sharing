class FindSecret:
    def __init__(self, t, n, p, Y):
        self.t = t
        self.n = n
        self.p = p
        self.Y = Y
        self.x = [i for i in range(1, t)]

    def inverse(self, number):
        number = number % self.p
        for i in range(1, self.p):
            if (i * number) % self.p == 1:
                return i
        return -1

    def calculateMultiplication(self, i):
        temp = 1
        for j in range(self.p):
            if i != j:
                inv = self.inverse(self.x[j]-self.x[i])
                if inv == -1:
                    raise Exception(f"{self.p} is not invertible for sum numbers !!")
                temp *= inv * self.x[j]
        return temp
