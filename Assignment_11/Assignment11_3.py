sum = 0
count = 1

def sum_of_digits(no):

    no = str(no)
    
    global sum
    global count
    for i in range(no):
        if (count <= len(no)):
            sum = sum + count
            count = count + 1
            sum_of_digits(no)

    return sum
    
def main():

    
    sum_of_digits(3456)
    print(sum)

if __name__ == "__main__":
    main()