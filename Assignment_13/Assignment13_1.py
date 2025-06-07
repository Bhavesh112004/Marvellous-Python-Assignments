class BookStore:
    NoOfBooks = 0

    def __init__(self,N,A):
        self.Name = N
        self.Author = A
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        """self.Name = name
        self.Author = author"""
        print("Count of books : ",self.NoOfBooks )
        print("Name of book :",self.Name)
        print("Name of Author : ",self.Author)



def main():

    Book_Name1  = str(input("Enter the name of Book1 : "))
    Author_Name1  = str(input("Enter the name of author1 : "))

    Book_Name2  = str(input("Enter the name of Book2 : "))
    Author_Name2  = str(input("Enter the name of author2 : "))

    Obj1 = BookStore(Book_Name1,Author_Name1)
    Obj1.Display()

    Obj2 = BookStore(Book_Name2,Author_Name2)
    Obj2.Display() 


if __name__ == "__main__":
    main()