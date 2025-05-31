import threading

def EvenNo(no):
    for i in range (2,no+1,2):
        print("The first ",no,"even numbers are: ",i)
    print("--------------------------------")
    
def OddNo(no):
    for i in range(1,no+1,2):
        print("The first ",no,"odd numbers are: ",i)

def main():
    
    t1 = threading.Thread(target = EvenNo, args= EvenNo(20))
    t2 = threading.Thread(target = OddNo, args = OddNo(20))

    t1.start
    t2.start

    t1.join
    t2.join

if __name__ == "__main__":
    main()