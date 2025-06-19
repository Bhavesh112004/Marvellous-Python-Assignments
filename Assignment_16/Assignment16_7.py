def ReadNameMarks(file_name):

    my_dict = {}

    Fobj = open(file_name,"r")
    
    for line in Fobj:
        parts = line.strip().split()
        print(parts)
        if len(parts) == 3:
            name, mark = parts[0], parts[2]
            if mark.isdigit():
                my_dict[name] = int(mark)

    print("Students who scored more than 75 marks:")
    for name, mark in my_dict.items():
        if mark > 75:
            print(f"{name}: {mark}")

def main():

    ReadNameMarks("marks.txt")

if __name__ == "__main__":
    main()