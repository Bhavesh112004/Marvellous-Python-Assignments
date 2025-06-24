def CompareContent(file_name1, file_name2):

    Fobj1 = open(file_name1,"r")
    Fobj2 = open(file_name2,"r")

    Data1 = Fobj1.read()
    Data2 = Fobj2.read()

    if Data1 not in Data2:
        print("Failure")
    else:
        print("Success")

def main():

    CompareContent("ABC.txt","ABC_copy.txt")

if __name__ == "__main__":
    main()