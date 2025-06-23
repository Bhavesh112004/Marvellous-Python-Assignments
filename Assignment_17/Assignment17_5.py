import schedule
import time
import datetime



def MySchedule():

    Fobj = open('Marvellous.txt','w')

    current_time = datetime.datetime.now()
    Fobj.write(str(current_time))

    Fobj.close()

def main():

    print("Inside the automation script : ")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(5).seconds.do(MySchedule)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()