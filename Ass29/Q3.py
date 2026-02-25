import sys
import os

if len(sys.argv) != 2:
    print("Usage: python script.py <source_file>")
    exit()

source_file = sys.argv[1]
destination_file = "Demo.txt"

if not os.path.isfile(source_file):
    print("Source file does not exist.")
    exit()

with open(source_file, 'r') as src:
    content = src.read()

with open(destination_file, 'w') as dest:
    dest.write(content)

print("Contents copied successfully to Demo.txt")