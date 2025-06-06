class Arithmatic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self,val1,val2):
        self.Value1 = val1
        self.Value2 = val2

    def Addition(self):
        result = self.Value1 + self.Value2
        print("The Addition of numbers is : ",result)

    def Substarction(self):
        result = self.Value1 - self.Value2
        print("The Substarction of numbers is : ",result)

    def Multiplication(self):
        result = self.Value1 * self.Value2
        print("The Addition of numbers is : ",result)

    def Division(self):
        result = self.Value1 / self.Value2
        print("The Addition of numbers is : ",result)

def main():

    val1 = int(input("Enter the first value  : "))
    val2 = int(input("Enter the second value : "))

    A = Arithmatic()

    A.Accept(val1,val2)
    A.Addition()
    A.Substarction()
    A.Multiplication()
    A.Division()




if __name__ == "__main__":
    main()