import sys

def CopyFile(SourceFile,DestinationFile):

    Fobj = open(SourceFile,"r")
    Fobj1 = open(DestinationFile,"w")

    Data = Fobj.read()
    for data in Data:
        Fobj1.write(data)

    Fobj.close()
    Fobj1.close()

    #Copy_data = Fobj1.read()
    #print(copy_data)

def main():

    

    CopyFile("Demo.txt", sys.argv[1])


if __name__ == "__main__":
    main()



