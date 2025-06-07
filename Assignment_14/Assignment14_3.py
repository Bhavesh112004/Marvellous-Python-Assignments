class Book:

    def __init__(self,P):
        self.__price = P

    def get_price(self):

        print("Inside get method : ",self.__price)

    def set_price(self,new_price):
        self.__price = self.__price + new_price
        print("The price of book after set price : ",self.__price)

def main():

    book_price = int(input("Enter the price of a book : "))
    inc_price = int(input("Enter the amount to add to price : "))

    Obj = Book(book_price)
    Obj.get_price()
    Obj.set_price(inc_price)

if __name__ == "__main__":
    main()

