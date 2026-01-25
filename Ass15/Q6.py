from functools import reduce
No = list(map(int,input("Enter the Number separated by space :").split()))
min = reduce(lambda x , y : x if x < y else y , No)
print("Minimum number from the list :",min)