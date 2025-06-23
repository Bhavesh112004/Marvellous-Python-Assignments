import schedule
import datetime
import time
import os
import shutil


SOURCE_DIR = r'C:\Users\ahire\OneDrive\Desktop\Assignment_17\source_folder'
BACKUP_DIR = r"C:\Users\ahire\OneDrive\Desktop\Assignment_17\backup_folder"
LOG_FILE = "backup_log.txt"

def BackupFiles():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_subdir = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
    
    try:
        shutil.copytree(SOURCE_DIR, backup_subdir)

        Fobj = open(LOG_FILE, "a")
        Fobj.write(f"[{timestamp}] Backup successful: {backup_subdir}\n")
        Fobj.close()

        print(f"Backup completed successfully at {timestamp}")
    
    except Exception as e:
        Fobj = open(LOG_FILE, "a")
        Fobj.write(f"[{timestamp}] Backup failed: {str(e)}\n")
        Fobj.close()

        print(f"Backup failed at {timestamp}: {e}")

def main():
    print("Inside the automation script")
    print("Current date and time is :", datetime.datetime.now())

    # Schedule backup function every hour
    schedule.every(1).minutes.do(BackupFiles)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
