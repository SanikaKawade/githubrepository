# Class Definition
class Demo:
    # Class variable
    Value = 0

    # Constructor
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    # Instance Method 1
    def Fun(self):
        print("Inside Fun()")
        print("Value of no1:", self.no1)
        print("Value of no2:", self.no2)

    # Instance Method 2
    def Gun(self):
        print("Inside Gun()")
        print("Value of no1:", self.no1)
        print("Value of no2:", self.no2)


# Creating Objects
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

# Calling Methods
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()