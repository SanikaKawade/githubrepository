from functools import reduce
No = list(map(int,input("Enter the Number separated by space :").split()))
add = reduce(lambda x , y : x + y , No)
print("Addition of all numbers from the list :",add)