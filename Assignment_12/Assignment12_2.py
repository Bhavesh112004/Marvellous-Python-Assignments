class Circle:
    PI = 3.14

    def __init__(self):
        
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumferance = 0.0

    
    def Accept(self,rad):
        self.Radius = rad
        
        
   
    def CalculateArea(self):
        result = self.PI * self.Radius * self.Radius
        self.Area = result
        

    
    def CalculateCircumferance(self):
        
        result = 2 * self.PI * self.Radius
        self.Circumferance = result
        

    
    def Display(self):
       print("Radius = ",self.Radius)
       print("Circumferance = ",self.Circumferance)
       print("Area = ",self.Area)





def main():
    rad = int(input("Enter the Radius of the circle : "))

    c= Circle()

    
    c.Accept(rad)
    c.CalculateArea()
    c.CalculateCircumferance()
    c.Display()



if __name__ == "__main__":
    main()