class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price


def main():

    Obj1 = Product("Tomato 1 kg",60)
    Obj2 = Product("onion 2 kg",60)

    print(Obj1 == Obj2)

if __name__ == "__main__":
    main()

