class Person:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age

    def Display(self):
        print("Name : ",self.Name)
        print("Age : ",self.Age)
    
class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.Subject = subject
        self.Salary = salary

    def Display(self):
        super().Display()
        print("Subject : ",self.Subject)
        print("Salary : ",self.Salary)

def main():

    Obj = Teacher("Piyush sir",35,"Data Science",50000000000)
    Obj.Display()

if __name__ == "__main__":
    main()
