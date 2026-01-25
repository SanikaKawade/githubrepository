No = list(map(int,input("Enter the Number separated by space :").split()))
count = len(list(filter(lambda No : No % 2 == 0 , No)))
print("Even  numbers count from the list :",count)