No = list(map(int,input("Enter the Number separated by space :").split()))
div = list(filter(lambda No : No % 3 == 0  and No % 5 == 0 , No))
print(" numbers divisible by 3 and from the list :",div)