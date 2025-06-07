class Vehicle:
    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def start(self):
        super().start()  
        print("Car engine started with push button.")  


def main():

    Obj = Car()
    Obj.start()

if __name__ == "__main__":
    main()

