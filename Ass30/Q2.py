filename = input("Enter file name: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        print("Total number of words:", len(words))
except FileNotFoundError:
    print("File does not exist.")