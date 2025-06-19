i = 1

def PrintNumbers(no):
    
    global i
    if (i <= no):
        print(i, end = " ")
        i = i + 1
        PrintNumbers(no)


def main():

    PrintNumbers(5)


if __name__ == "__main__":
    main()