# Accept file name and word from user
filename = input("Enter file name: ")
word_to_search = input("Enter word to search: ")

found = False

try:
    with open(filename, 'r') as file:
        # Read file line by line
        for line in file:
            words = line.split()
            if word_to_search in words:
                found = True
                break

    if found:
        print(f"The word '{word_to_search}' is found in {filename}.")
    else:
        print(f"The word '{word_to_search}' is NOT found in {filename}.")

except FileNotFoundError:
    print("File not found. Please check the file name.")