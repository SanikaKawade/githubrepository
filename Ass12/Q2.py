No = int(input("Enter the number :"))
fact = 1
for i in range(1, No+1):
    fact = fact * i
    print(" its factors :",i)
print("Factorial of ",No,"is :",fact)
