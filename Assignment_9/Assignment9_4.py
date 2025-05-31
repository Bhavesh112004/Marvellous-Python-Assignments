import multiprocessing
import threading
import time

def SumOfNumbers(no):
    sum = 0
    for i in range (1,no+1,1):
        sum = sum + i
    return(sum)



def main():
    
    start_time = time.time()
    ret = SumOfNumbers(100000000)
    #print(ret)
    end_time = time.time()
    print("Time required for execution using normal function : ",end_time - start_time)

    start_time1 = time.time()
    t1 = threading.Thread(target = SumOfNumbers, args = SumOfNumbers(100000000))
    t1.start
    t1.join
    end_time1 = time.time()
    print("Time required for the execution using multithreading is : ",end_time1 - start_time1)

    start_time2 = time.time()
    p1 = multiprocessing.Process(target = SumOfNumbers, args = (100000000,))
    p1.start
    p1.join
    
    end_time2 = time.time()
    print("Time required for the execution using multiprocessing is : ",end_time2 - start_time2)




    

if __name__ == "__main__":
    main()