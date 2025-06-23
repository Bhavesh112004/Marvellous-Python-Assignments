import schedule
import time
import datetime

def Myschedule():

    print("Executing task daily at 9 AM")
    


def main():
    print("Inside the automation script : ")
    print("Current time is : ",datetime.datetime.now())

    schedule.every().day.at("09:00").do(Myschedule)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()