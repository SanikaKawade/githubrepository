def MaxList():
    n = int(input("Enter the number of elements :"))
    numbers = []

    for i in range(n):
        num = float(input(f"Enter Elements {i + 1} :"))
        numbers.append(num)

    maximum = max(numbers)
    print("Maximum number from the list is :",maximum)

MaxList()