def Sum_Digits(n):
    total = 0

    while n != 0 :
        total += n % 10
        n = n // 10
    return total

num = int(input("Enter number  :"))
print("Sum of Digits :",Sum_Digits(num))