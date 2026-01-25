def frequency():
    n = int(input("Enter the number of elements :"))
    numbers = []

    for i in range(n):
        num = float(input(f"Enter Elements {i + 1} :"))
        numbers.append(num)

    target = float(input("Enter the number to find its frequency :"))

    freq = numbers.count(target)
    print(f"the number {target} appears {freq} times in the list ")

frequency()