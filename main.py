from make_function import MakeFunction


if __name__ == '__main__':
    make = MakeFunction(n=4, t=3, S=10, p=13)
    make.generateFunction()
    Y = make.getShares()
    print(Y)
