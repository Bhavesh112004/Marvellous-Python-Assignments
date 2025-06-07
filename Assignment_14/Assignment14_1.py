class Employee:

    def __init__(self,name,emp_id,salary):
        self.Name = name
        self.ID = emp_id
        self.salary = salary

    def Display(self):
        print("Employee Name is : ",self.Name)
        print("Employee Id is : ",self.ID)
        print("Employee Salary is : ",self.salary)

def main():

    Obj = Employee("Rohit",101,50000)
    Obj.Display()


if __name__ == "__main__":
    main()

