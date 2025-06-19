def CopyContent(SourceFile , DestinationFile):

    Fobj1 = open(SourceFile,"r")
    Fobj2 = open(DestinationFile,"w")

    Data1 = Fobj1.read()
    
    for data in Data1:
        Fobj2.write(data)

def main():
    
    CopyContent("source.txt","destination.txt")
   
if __name__ == "__main__":
    main()