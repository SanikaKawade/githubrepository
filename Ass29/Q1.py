import os

filename = input("Enter file name: ")

if os.path.isfile(filename):
    print(f"{filename} exists in the current directory.")
else:
    print(f"{filename} does not exist in the current directory.")