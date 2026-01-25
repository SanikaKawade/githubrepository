No = list(map(int,input("Enter the Number separated by space :").split()))
odd = list(filter(lambda No : No % 2 != 0 , No))
print("Odd numbers from the list :",odd)