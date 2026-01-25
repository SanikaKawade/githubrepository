import threading

def evenlist(data):
    even_sum = 0
    print("Even elements:")
    for i in data:
        if i % 2 == 0:
            print(i, end=" ")
            even_sum += i
    print("\nSum of even elements =", even_sum)

def oddlist(data):
    odd_sum = 0
    print("Odd elements:")
    for i in data:
        if i % 2 != 0:
            print(i, end=" ")
            odd_sum += i
    print("\nSum of odd elements =", odd_sum)

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input(f"Enter element {i+1}: ")))

t1 = threading.Thread(target=evenlist, args=(lst,), name="EvenList")
t2 = threading.Thread(target=oddlist, args=(lst,), name="OddList")

t1.start()
t2.start()

t1.join()
t2.join()