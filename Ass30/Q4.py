import os

source_file = input("Enter existing file name: ")
destination_file = input("Enter new file name: ")

if not os.path.isfile(source_file):
    print("Source file")