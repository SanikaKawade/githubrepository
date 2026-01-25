def SumFactors(n):
    total = 0
    for i in range(1,n+1):
        if n % i == 0 :
            total = total + i
    return total

num = int(input("Enter the number :"))
print(SumFactors(num))