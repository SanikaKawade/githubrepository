filename = input("Enter file name: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile Contents:\n")
        print(content)
except FileNotFoundError:
    print(f"{filename} does not exist.")
except Exception as e:
    print("An error occurred:", e)