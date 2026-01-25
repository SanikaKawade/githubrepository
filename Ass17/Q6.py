def pattern(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end="  ")
        print()

num = int(input("Enter number of rows :"))
pattern(num)