No = list(map(int,input("Enter the Number separated by space :").split()))
even = list(filter(lambda No : No % 2 == 0 , No))
print("Even numbers from the list :",even)