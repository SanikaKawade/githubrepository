import threading

def isprime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def prime_list(data):
    print("Prime numbers:")
    for i in data:
        if isprime(i):
            print(i, end=" ")
    print()

def nonprime_list(data):
    print("Non-prime numbers:")
    for i in data:
        if not isprime(i):
            print(i, end=" ")
    print()

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input(f"Enter element {i+1}: ")))

t1 = threading.Thread(target=prime_list, args=(lst,), name="Prime")
t2 = threading.Thread(target=nonprime_list, args=(lst,), name="NonPrime")

t1.start()
t2.start()

t1.join()
t2.join()