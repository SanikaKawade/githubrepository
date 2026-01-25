import threading

sum_result = 0
prod_result = 1

def sum_list(data):
    global sum_result
    sum_result = sum(data)

def prod_list(data):
    global prod_result
    prod_result = 1
    for i in data:
        prod_result *= i

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input(f"Enter element {i+1}: ")))

t1 = threading.Thread(target=sum_list, args=(lst,), name="SumThread")
t2 = threading.Thread(target=prod_list, args=(lst,), name="ProdThread")

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum of elements =", sum_result)
print("Product of elements =", prod_result)