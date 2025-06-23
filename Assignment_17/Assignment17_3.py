import schedule
import time
import datetime

def Myschedule():

    print("Current data and time is : ",datetime.datetime())
    print("Do Coding..")
    


def main():
    print("Inside the automation script : ")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(30).minutes.do(Myschedule)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()