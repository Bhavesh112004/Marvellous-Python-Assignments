class Calculator:

    def __init__(self,num1,num2):
        self.Number1 = num1
        self.Number2 = num2

    def Addition(self):
        result = self.Number1 + self.Number2
        print("The addition of two numbers is : ",result)

    def Substarction(self):
        result = self.Number1 - self.Number2
        print("The substraction of two umbers is : ",result)

    def Multiplication(self):
        result = self.Number1 * self.Number2
        print("The multiplition of two umbers is : ",result)

    def Division(self):
        result = self.Number1 / self.Number2
        print("Thedivision of two numbers is : ",result)

def main():

    no1 = int(input("Enter the first number  : "))
    no2 = int(input("Enter the second number : "))

    Obj = Calculator(no1,no2)
    Obj.Addition()
    Obj.Substarction()
    Obj.Multiplication()
    Obj.Division()

if __name__ == "__main__":
    main()

