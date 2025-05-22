def Pattern(no):
    for row in range(1,no+1,1):
        for column in range(1,row+1,1):
            print("*",end = " ")
        print()


def main():

    ret = Pattern(4)
    
if __name__ == "__main__":
    main()