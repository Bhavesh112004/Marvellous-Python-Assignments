import threading

def EvenList(lst):
    sum = 0
    for i in lst:
        if (i % 2 == 0):
            sum = sum + i
    print(sum)

def OddList(lst):
    sum = 0
    for i in lst:
        if (i == 1):
            sum = sum + i
        if (i % 3 == 0):
            sum = sum + i
    print(sum)

def main():

    data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    t1 = threading.Thread(target = EvenList, args = EvenList(data))
    t2 = threading.Thread(target = OddList, args = OddList(data))

    t1.start
    t2.start

    t1.join
    t2.join


if __name__ == "__main__":
    main()