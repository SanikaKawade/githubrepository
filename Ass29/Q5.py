filename = input("Enter file name: ")
search_string = input("Enter string to search: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        count = content.count(search_string)
        print(f'"{search_string}" appears {count} times in {filename}')
except FileNotFoundError:
    print("File does not exist.")