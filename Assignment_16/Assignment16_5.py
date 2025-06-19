def ReadContent(file_name):

    Fobj = open(file_name, "r")

    lines = Fobj.readlines()

    for line in lines:
        words = line.split()
        cnt = len(words)
        print("count of word in this line is : ",cnt)
        if (cnt > 5):
            print(words)
            
def main():

    ReadContent("Sample.txt")

if __name__ == "__main__":
    main()