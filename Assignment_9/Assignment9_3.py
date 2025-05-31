import os
import time
import multiprocessing

def Factorial(no):
    fact = 1
    count = 1
    while (count <= no):
        fact = fact * count
        count = count + 1
    return fact


def main():

    data = [5,6,7,8,9,10]

    result = []

    p = multiprocessing.Pool()
    result = p.map(Factorial,data)

    p.close
    p.join

    print(result)
    
if __name__ == "__main__":
    main()