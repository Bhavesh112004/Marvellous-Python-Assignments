def Read_Display(file_name):

    Fobj = open(file_name,"r")

    data = Fobj.read()
    print("The content in the file is : ",data)

def main():

    Read_Display("data.txt")

if __name__ == "__main__":
    main()