import threading


def Display1(no):
    for i in range(1,no+1,1):
        print(i)

def Display2(no):
    for i in range(no,0,-1):
        print(i)


def main():

    t1 = threading.Thread(target = Display1, args = Display1(50))
    t1.start
    print("Thread 1 execution completed here")

    t2 = threading.Thread(target = Display2, args = Display2(50) )
    t2.start
    print("Thread 2 execution completed here")

    t1.join
    t2.join
    print("Main thread exited here")
    

if __name__ == "__main__":
    main()