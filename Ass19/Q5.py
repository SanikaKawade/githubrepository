from functools import reduce
def isprime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

data = [2, 70, 11, 10, 17, 23, 31, 77]

# Filter prime numbers
filtered = list(filter(isprime, data))
print("List after filter =", filtered)

# Multiply each number by 2
mapped = list(map(lambda x: x * 2, filtered))
print("List after map =", mapped)

# Find maximum number
result = reduce(lambda a, b: a if a > b else b, mapped)
print("Output of reduce =", result)