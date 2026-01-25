def square(n):
    for i in range(n):
        for j in range(n):
            print("*",end="  ")
        print()

num = int(input("Enter the number :"))
square(num)