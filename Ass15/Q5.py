from functools import reduce
No = list(map(int,input("Enter the Number separated by space :").split()))
max = reduce(lambda x , y : x if x > y else y , No)
print("Maximum number from the list :",max)