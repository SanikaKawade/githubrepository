import threading

def even():
    print("Even thread:")
    for i in range(2, 21, 2):
        print(i, end=" ")
    print()

def odd():
    print("Odd thread:")
    for i in range(1, 20, 2):
        print(i, end=" ")
    print()

t1 = threading.Thread(target=even, name="Even")
t2 = threading.Thread(target=odd, name="Odd")

t1.start()
t2.start()

t1.join()
t2.join()