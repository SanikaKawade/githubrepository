def Count_Digits(n):
    count = 0

    while n != 0 :
        n = n // 10
        count += 1
    return count

num = int(input("Enter number  :"))
print("Number of Digits :",Count_Digits(num))