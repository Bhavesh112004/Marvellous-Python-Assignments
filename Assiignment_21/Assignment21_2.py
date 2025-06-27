import psutil
import time

def ProcessDisplay():

    timestamp = time.ctime()
    Border = "-"*90

    file_name = "Process%s.log" % timestamp
    file_name = file_name.replace(" ","_")
    file_name = file_name.replace(":","_")
    
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

    Border = "-"*90
    print(Border)
    print("Information of currently running processess: ")
    print(Border)


    ProcessDisplay()

if __name__ == "__main__":
    main()