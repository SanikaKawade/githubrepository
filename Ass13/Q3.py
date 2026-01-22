No = int(input("Enter the number :"))
sum_of_divisors = 0

for i in range(1,No):
    if No % i == 0 :
        sum_of_divisors += i

if sum_of_divisors == No :
    print(No,"is a perfect number")
else :
    print(No,"is not a perfect number")