def PatternPrint(n):
    for i in range(0,n,1):
        for j in range(1,n-i,1):
            print("*",end ="" )
        print("*")    

def main():
    PatternPrint(5)

if __name__ == "__main__":
    main()