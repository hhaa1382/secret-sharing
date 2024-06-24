class FindSecret:
    def __init__(self, t, n, p, Y):
        self.t = t
        self.n = n
        self.p = p
        self.Y = Y

    def inverse(self, number):
        number = number % self.p
        if number == 0:
            return 0
        for i in self.p:
            if (i*number)%self.p == 1:
                return i
        return -1
