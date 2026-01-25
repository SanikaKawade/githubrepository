from functools import reduce
No = list(map(int,input("Enter the Number separated by space :").split()))
pro = reduce(lambda x , y : x * y , No)
print("product of all numbers from the list :",pro)