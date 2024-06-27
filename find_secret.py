class FindSecret:
    def __init__(self, t, n, p, Y, X):
        self.t = t
        self.n = n
        self.p = p
        self.Y = Y

        if X is None:
            self.x = [i+1 for i in range(0, t)]
        else:
            self.x = X

    def inverse(self, number):
        number = number % self.p
        if number == 0:
            return 0
        for i in range(1, self.p):
            if (i * number) % self.p == 1:
                return i
        return -1

    def calculateMultiplication(self, i):
        temp = 1
        for j in range(self.t):
            if i != j:
                inv = self.inverse(self.x[j]-self.x[i])
                if inv == -1:
                    raise Exception(f"{self.p} is not invertible for some numbers !!")
                temp *= inv * self.x[j]
        return temp % self.p

    def calculateSecret(self):
        s = 0
        for i in range(len(self.Y)):
            s += self.Y[i] * self.calculateMultiplication(i)
        return s % self.p
