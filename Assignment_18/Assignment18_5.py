def StringFrequency(file_name, String):

    Fobj1 = open(file_name,"r")

    data = Fobj1.read()
    word = data.split()
    count = 0
    for everyword in word:
        if (everyword == String):
            count = count + 1

    print(count)


def main():

    file_name = input()
    string = input()

    StringFrequency(file_name,string)

if __name__ == "__main__":
    main()