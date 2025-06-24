import sys

def CopyFileContent(original_file, copied_file):

    Fobj1 = open(original_file,"r")
    Fobj2 = open(copied_file,"w")

    Data = Fobj1.read()
    for data in Data:
        Fobj2.write(data)

def main():

    CopyFileContent("ABC.txt",sys.argv[1])

if __name__ == "__main__":
    main()