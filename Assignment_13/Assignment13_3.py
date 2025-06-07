class Numbers:

    def __init__(self,value_user):
        self.Value = value_user

    def ChkPrime(self):
        if (self.Value == 2):
            print(" The number is prime")

        for i in range(2,self.Value):
            if ((self.Value % i) == 0):
                print("The number is not prime")
                break
                
            else:
                print("Prime")
                break

    def Factors(self):
        self.List = []
        for i in range(1,(self.Value+1)):
            if ((self.Value % i) == 0):
                self.List.append(i)

        print("The list of factors of the given number : ",self.List)
        
    def SumFactors(self):
        self.Sum = 0
        for i in self.List:
            if(i == self.Value):
                break
            self.Sum = self.Sum + i

        print("The sum of factors excluding number itself : ",self.Sum)

    def ChkPerfect(self):
        if (self.Sum == self.Value):
            print("The given number is perfect number ")

        else:
            print("The given number is not a perfect number")

def main():

    num = int(input("Enter the Number : "))

    c = Numbers(num)
    c.ChkPrime()
    
    c.Factors()
    c.SumFactors()
    c.ChkPerfect()

if __name__ == "__main__":
    main()