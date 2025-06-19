def WriteNumbers(file_name,numbers_list):

    Fobj = open(file_name,"w")

    for number in numbers_list:
        Fobj.write(str(number))
        Fobj.write("\n")

    Fobj.close()

def main():

    lst = []
    for i in range(1,11):
        no = int(input())
        lst.append(no)
    
    WriteNumbers("numbers.txt",lst)

if __name__ == "__main__":
    main()