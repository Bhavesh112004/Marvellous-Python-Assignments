import threading

def EvenFactor(no):
    sum = 0
    for i in range(2,no+1,2):
        if (no % i == 0):
            sum = sum + i
    print(sum)

def OddFactor(no):
    sum = 0
    for i in range(1,no+1,2):
        if (no % i == 0):
            sum = sum + i
    print(sum)


def main():

    t1 = threading.Thread(target = EvenFactor, args = EvenFactor(20))
    t2 = threading.Thread(target = OddFactor, args = OddFactor(21))

    t1.start
    t2.start

    t1.join
    t2.join

    print("The main thread ends here")


if __name__ == "__main__":
    main()