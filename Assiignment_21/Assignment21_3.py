import psutil
import time
import os
import sys

def CreateLogDirectory(FolderName):

    if not os.path.exists(FolderName):
        os.mkir(FolderName)

    timestamp = time.ctime()
    Border = "-"*90

    file_name = "Process%s.log" % timestamp
    file_name = file_name.replace(" ","_")
    file_name = file_name.replace(":","_")

    file_name = os.path.join(FolderName, file_name)
    
    fobj = open(file_name,"w")

    fobj.write(Border+"\n")
    fobj.write("-----------------------------Welcome to the ProcessInfo automation script-----------------------------------\n")
    fobj.write(Border+"\n\n")

    for proc in psutil.process_iter():
        if(proc.is_running()):
            try:
                info = proc.as_dict(attrs=['pid','name','username'])
                info['vms'] = proc.memory_info().vms / (1024 * 1024)
                fobj.write(str(info)+"\n")
            except Exception:
                print("Exception occured")

        else: 
            print("Process is not running")


    fobj.write(Border+"\n")
    fobj.write("-----------------------------------------End of Automation script ---------------------------\n")
    fobj.write("-----------------------------------Thanks for using the automation script-----------------------------------------\n")
    print(Border+"\n")

def main():

    
    if (len(sys.argv)== 2):
        if(sys.argv[1] == "--h" or sys.argv[1]== "--H"):
            print("This is the process automation script")
            print("It writes the running processes in the directory mentioned")

        elif(sys.argv[1]== "--u" or sys.argv[1]== "--U"):
            print("This script can be used as : ")
            print("program_name DirectoryName")

        else:
            CreateLogDirectory(sys.argv[1])
            Border = "-"*90
            print(Border)
            print("Information of currently running processess: ")
            print(Border)

    else:
        print("Invalid number of arguments")
        print("Use --h : for help")
        print("Use --u : for usage")



if __name__ == "__main__":
    main()