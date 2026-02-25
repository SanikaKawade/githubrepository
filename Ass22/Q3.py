# Class Definition
class Arithmetic:

    # Constructor
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    # Accept values from user
    def Accept(self):
        self.Value1 = float(input("Enter first value: "))
        self.Value2 = float(input("Enter second value: "))

    # Addition
    def Addition(self):
        return self.Value1 + self.Value2

    # Subtraction
    def Subtraction(self):
        return self.Value1 - self.Value2

    # Multiplication
    def Multiplication(self):
        return self.Value1 * self.Value2

    # Division (handle division by zero)
    def Division(self):
        if self.Value2 == 0:
            return "Error: Division by zero not allowed"
        else:
            return self.Value1 / self.Value2


# Creating multiple objects
obj1 = Arithmetic()
obj2 = Arithmetic()

# For first object
print("Enter values for first object")
obj1.Accept()
print("Addition:", obj1.Addition())
print("Subtraction:", obj1.Subtraction())
print("Multiplication:", obj1.Multiplication())
print("Division:", obj1.Division())
print("----------------------------")

# For second object
print("Enter values for second object")
obj2.Accept()
print("Addition:", obj2.Addition())
print("Subtraction:", obj2.Subtraction())
print("Multiplication:", obj2.Multiplication())
print("Division:", obj2.Division())