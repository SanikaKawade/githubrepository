import threading

def evenfactor(no):
    sum_even = 0
    print("Even factors:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i, end=" ")
            sum_even += i
    print("\nSum of even factors =", sum_even)

def oddfactor(no):
    sum_odd = 0
    print("Odd factors:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i, end=" ")
            sum_odd += i
    print("\nSum of odd factors =", sum_odd)

num = int(input("Enter number: "))

t1 = threading.Thread(target=evenfactor, args=(num,), name="EvenFactor")
t2 = threading.Thread(target=oddfactor, args=(num,), name="OddFactor")

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")