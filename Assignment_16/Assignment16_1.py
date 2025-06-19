def CreateFile(file_name):

    Fobj = open(file_name,"w")

    Fobj.write("1. Bhavesh\n")
    Fobj.write("2. Rohan\n")
    Fobj.write("3. Om\n")
    Fobj.write("4. Prajyot\n")
    Fobj.write("5. Aadesh")


def main():

    CreateFile("student.txt")

if __name__ == "__main__":
    main()