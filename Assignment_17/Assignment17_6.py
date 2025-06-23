import schedule
import datetime
import time

def LunchTime():

    print("Lunch Time!")

def WrapWork():

    print("Wrap up work")

def main():

    print("Inside the automation script")
    print("Current date and time is : ",datetime.datetime.now())

    schedule.every().day.at("01:00").do(LunchTime)
    schedule.every().day.at("09:00").do(WrapWork)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()