from make_function import MakeFunction
from find_secret import FindSecret


def getValue(str):
    print(f"Enter {str} : ")
    return int(input())


if __name__ == '__main__':
    while True:
        print("1- get n shares\n2-get secret\n")
        num = int(input())
        try:
            if num == 1:
                t = getValue("t")
                n = getValue("n")
                S = getValue("S")
                p = getValue("p")

                make = MakeFunction(n=n, t=t, S=S, p=p)
                make.generateFunction()
                Y = make.getShares()
                print(f"Shares : {Y}\n\n")
                make.plotValues(Y)

            elif num == 2:
                t = getValue("t")
                n = getValue("n")
                p = getValue("p")

                print(f"Enter Y (values separate by ,) : ")
                Y = input()

                find = FindSecret(n=n, t=t, Y=[int(y) for y in Y.split(",")], p=13)
                S = find.calculateSecret()
                print(f"Secret is : {S}\n\n")

            else:
                break

        except:
            print("an error occurs!")
