def RemoveBlankLines(file,CleanedFile):

    Fobj = open(file,"r")
    Fobj1 = open(CleanedFile, "w")

    for line in Fobj:
        if line.strip():
            Fobj1.write(line)
            
def main():

    RemoveBlankLines('IncBlankLines.txt', 'IncBlankLinesCleaned.txt')

if __name__ == "__main__":
    main()