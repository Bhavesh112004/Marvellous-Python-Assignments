class Student:
    school_name = "The world school"  

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Student Name:", self.name)
        print("Roll No:", self.roll_no)
        print("School Name:", Student.school_name)

def main():


    Obj = Student("Rohan",34)
    Obj.display()

    Student.school_name = "Kendriya Vidyalaya"

    Obj1 = Student("Mohan",23)
    Obj1.display()


if __name__ == "__main__":
    main()