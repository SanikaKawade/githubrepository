from functools import reduce
data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

# Filter numbers between 70 and 90
filtered = list(filter(lambda x: x >= 70 and x <= 90, data))
print("List after filter =", filtered)

# Increase each number by 10
mapped = list(map(lambda x: x + 10, filtered))
print("List after map =", mapped)

# Product of all numbers
result = reduce(lambda a, b: a * b, mapped)
print("Output of reduce =", result)