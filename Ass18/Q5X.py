import MarvellousNumQ5
def listprime():
    n = int(input("Enter the number of elements: "))
    numbers = []

    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        numbers.append(num)

    prime_sum = 0
    for num in numbers:
        if MarvellousNumQ5.checkprime(num):
            prime_sum += num

    print("Sum of all prime numbers in the list is:", prime_sum)

listprime()