import sys
import os

if len(sys.argv) != 3:
    print("Usage: python script.py <file1> <file2>")
    exit()

file1 = sys.argv[1]
file2 = sys.argv[2]

if not os.path.isfile(file1) or not os.path.isfile(file2):
    print("One or both files do not exist.")
    exit()

with open(file1, 'r') as f1, open(file2, 'r') as f2:
    if f1.read() == f2.read():
        print("Success")
    else:
        print("Failure")