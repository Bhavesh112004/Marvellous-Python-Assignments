def AcceptName(String):
    print(len(String))

def main():
    print("Enter the name: ")

    name = str(input())

    result  = AcceptName(name)

if __name__ == "__main__":
    main()