class FindSecret:
    def __init__(self, t, n, p, Y):
        self.t = t
        self.n = n
        self.p = p
        self.Y = Y
        self.x = [i for i in range(1, n)]

    def inverse(self, number):
        number = number % self.p
        for i in range(1, self.p):
            if (i * number) % self.p == 1:
                return i
        return -1
