class Employee:
    def __init__(self, name, department, salary):
        self.name = name                # Public
        self._department = department  # Protected
        self.__salary = salary         # Private

    def Display(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Salary:", self.__salary)

def main():

    Obj = Employee("Rohan","Management",30000)
    Obj.Display()

    print(Obj.name)
    print(Obj._department)
    print(Obj._Employee__salary)

    

    

if __name__ == "__main__":
    main()

