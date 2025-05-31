import threading

def small(string):
    cnt = 0
    for i in string:
        if i .islower():
            cnt = cnt + 1
    print("No of lower case elements is : ",cnt)

def capital(string):
    cnt = 0
    for i in string:
        if i .isupper():
            cnt = cnt + 1
    print("No of upper case elements is : ",cnt)

def number(string):
    cnt = 0
    for i in string:
        if i .isdigit():
            cnt = cnt + 1
    print("No of digit elements is : ",cnt)


def main():

    data = "ABCDabchdi35u23"
    
    t1 = threading.Thread(target = small, args = small(data) )
    t2 = threading.Thread(target = capital, args = capital(data))
    t3 = threading.Thread(target = number, args = number(data))

    t1.start
    t2.start
    t3.start

    t1.join
    t2.join
    t3.join

if __name__ == "__main__":
    main()