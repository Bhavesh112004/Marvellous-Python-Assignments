import threading
import time

def PrintNumbers():
    for i in range (1,6,1):
        print(i)

    print("-----------------------------------")


def main():

    start_time = time.time()

    t1 = threading.Thread(target = PrintNumbers, args = PrintNumbers())
    t2 = threading.Thread(target = PrintNumbers, args= PrintNumbers())
    t3 = threading.Thread(target = PrintNumbers, args = PrintNumbers())

    t1.start
    time.sleep(1)

    t2.start
    time.sleep(1)

    t3.start

    t1.join
    t2.join
    t3.join

    end_time = time.time()

    print("The time required for the execution is : ",end_time-start_time)

    print("All threads execution ends here")


if __name__ == "__main__":
    main()