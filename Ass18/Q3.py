def MinList():
    n = int(input("Enter the number of elements :"))
    numbers = []

    for i in range(n):
        num = float(input(f"Enter Elements {i + 1} :"))
        numbers.append(num)

    minimum = min(numbers)
    print("Minimum number from the list is :",minimum)

MinList()