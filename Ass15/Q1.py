No = list(map(int,input("Enter the Number separated by space :").split()))
square = list(map(lambda No : No ** 2 , No))
print("Squares of numbers :",square)