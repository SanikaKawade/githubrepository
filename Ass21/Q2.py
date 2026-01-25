import threading

def maximum(data):
    print("Maximum element =", max(data))

def minimum(data):
    print("Minimum element =", min(data))

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input(f"Enter element {i+1}: ")))

t1 = threading.Thread(target=maximum, args=(lst,), name="MaxThread")
t2 = threading.Thread(target=minimum, args=(lst,), name="MinThread")

t1.start()
t2.start()

t1.join()
t2.join()