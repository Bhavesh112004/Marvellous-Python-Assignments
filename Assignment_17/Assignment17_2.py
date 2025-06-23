import schedule
import time
import datetime

def Myschedule():

    print("Inside MySchedule function at : ",datetime.datetime.now())
    


def main():
    print("Inside the automation script : ")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(1).minutes.do(Myschedule)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()