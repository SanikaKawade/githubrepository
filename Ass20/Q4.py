import threading

def small(string):
    count = 0
    for ch in string:
        if ch.islower():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of lowercase characters =", count)

def capital(string):
    count = 0
    for ch in string:
        if ch.isupper():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of uppercase characters =", count)

def digits(string):
    count = 0
    for ch in string:
        if ch.isdigit():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of digits =", count)

str1 = input("Enter a string: ")

t1 = threading.Thread(target=small, args=(str1,), name="Small")
t2 = threading.Thread(target=capital, args=(str1,), name="Capital")
t3 = threading.Thread(target=digits, args=(str1,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()