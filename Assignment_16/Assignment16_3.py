def ReadContent(file_name):

    Fobj = open(file_name, "r")

    data = Fobj.read()

    count_words = 0
    words = data.split()
    for word in words:
        count_words = count_words +1

    print("No of words in the file are : ",count_words)
    

    count_char = 0
    for char in data:
        split_data = data.split(" ")
        count_char = count_char + 1

    print("No of characters in the file are : ",count_char)

    count_lines = 0
    for line in data:
        if "\n" in line:
            count_lines = count_lines + 1

    print("No of lines in the file are : ",count_lines)

def main():

    ReadContent("Sample.txt")

if __name__ == "__main__":
    main()