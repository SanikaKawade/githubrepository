# Class Definition
class Circle:
    # Class variable
    PI = 3.14

    # Constructor
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    # Accept radius from user
    def Accept(self):
        self.Radius = float(input("Enter radius: "))

    # Calculate Area
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    # Calculate Circumference
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    # Display values
    def Display(self):
        print("Radius:", self.Radius)
        print("Area:", self.Area)
        print("Circumference:", self.Circumference)
        print("---------------------------")


# Creating multiple objects
obj1 = Circle()
obj2 = Circle()

# For first object
print("Enter details for first circle")
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

# For second object
print("Enter details for second circle")
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()