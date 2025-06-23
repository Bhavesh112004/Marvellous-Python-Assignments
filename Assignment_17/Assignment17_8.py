import schedule
import time
import datetime

def CheckEmail():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] Checking mail...")

def main():
    print("Email checker started.")
    schedule.every(10).seconds.do(CheckEmail)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
