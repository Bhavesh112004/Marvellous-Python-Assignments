def First10Even():
    count = 1
    no = 2
    while (count <= 10):
        if (no % 2 == 0):
           count = count + 1 
           print(no)
        
        no = no + 1

def main():
    result = First10Even()

if __name__ == "__main__":
    main()