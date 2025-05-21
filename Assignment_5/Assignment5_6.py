def Conversion(Celsius):

    DegFar = (Celsius * 9/5) + 32
    return DegFar

def main():

    print("Enter the temperature in degree celcius : ")
    Cel = int(input())

    ret = Conversion(Cel)
    print(ret," is the degree farhenhiet conversion of",Cel)

if __name__=="__main__":
    main()


