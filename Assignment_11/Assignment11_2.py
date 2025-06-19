i = 1
fact = 1


def Factorial(no):
    
    global i
    global fact
    if (i <= no):
        fact = fact * i
        i = i + 1
        Factorial(no)

    return fact



def main():

    Factorial(5)
    print(fact)


if __name__ == "__main__":
    main()