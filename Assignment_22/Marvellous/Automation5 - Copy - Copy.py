import schedule
import time
import datetime

def MySchedule():
    print("Inside MySchedule function at : ",datetime.datetime.now())

def MySchedulex():
    print("Inside MyScheduleX function",datetime.datetime.now())

def main():
    print("Inside automation script")
    print("Current time is : ",datetime.datetime.now())

    #schedule.every(20).seconds.do(MySchedule)
    #schedule.every(1).minute.do(MySchedulex)

    schedule.every(1).hour.do(MySchedulex)

    print("Application is in waitiong state")


    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()