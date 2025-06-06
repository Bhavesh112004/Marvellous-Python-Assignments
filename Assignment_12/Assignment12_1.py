class Demo:
    class_variable = "Value"

    def __init__(self,no1,no2):
        self.first_number = no1
        self.second_number = no2

    def Fun(self):
        print("The first number in Fun method : ",self.first_number)
        print("The second number in Fun method: ",self.second_number)

    def Gun(self):
        print("The first number in Gun method : ",self.first_number)
        print("The second number in Gun method: ",self.second_number)

def main():

    print("Enter the numbers : ")
    """num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())"""

    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()