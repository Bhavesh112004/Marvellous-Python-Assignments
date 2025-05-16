def PatternPrint(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(j,end ="" )
        print("")    

def main():
    PatternPrint(5)

if __name__ == "__main__":
    main()