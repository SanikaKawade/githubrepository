# Class Definition
class Numbers:

    # Constructor
    def __init__(self, Value):
        self.Value = Value

    # Check Prime
    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                return False
        return True

    # Display Factors
    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    # Sum of Factors
    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    # Check Perfect Number
    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False


# Creating multiple objects
obj1 = Numbers(6)
obj2 = Numbers(7)

print("For Number:", obj1.Value)
print("Prime:", obj1.ChkPrime())
print("Perfect:", obj1.ChkPerfect())
obj1.Factors()
print("Sum of factors:", obj1.SumFactors())
print("---------------------------")

print("For Number:", obj2.Value)
print("Prime:", obj2.ChkPrime())
print("Perfect:", obj2.ChkPerfect())
obj2.Factors()
print("Sum of factors:", obj2.SumFactors())