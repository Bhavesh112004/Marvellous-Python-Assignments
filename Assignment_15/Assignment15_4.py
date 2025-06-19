import sys

def CheckContent(First_File,Second_File):

    Fobj = open(First_File,"r")
    Fobj1 = open(Second_File,"r")

    Data1 = Fobj.read()
    Data2 = Fobj1.read()

    if (Data1 == Data2):
        print("Success")

    else:
        print("Failure")
        

    Fobj.close()
    Fobj1.close()

    
def main():

    ret = CheckContent("Demo.txt","ABC.txt")
    
if __name__ == "__main__":
    main()



