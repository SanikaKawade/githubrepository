def SumList():
    n = int(input("Enter the number of elements :"))
    numbers = []

    for i in range(n):
        num = float(input(f"Enter Elements {i + 1} :"))
        numbers.append(num)

    total = sum(numbers)
    print("the sum of the numbers in the list is :",total)

SumList()