def CheckFrequency(FileName,String):

    count = 0
    Fobj = open(FileName,"r")
    for everyline in Fobj:
        split_word = everyline.split()
        print(split_word)

        for word in split_word:
            if (word  == String):
                count = count + 1
        

        
    print("The frequencey of string in file is : ",count)

def main():

    file_name = input()
    string_name = str(input())

    CheckFrequency(file_name, string_name)

if __name__ == "__main__":
    main()