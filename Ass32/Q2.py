import os
import sys
import hashlib

def calculate_checksum(file_path):
    hash_obj = hashlib.md5()

    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            hash_obj.update(chunk)

    return hash_obj.hexdigest()


def find_duplicates(directory):
    files = {}
    duplicates = []

    for foldername, subfolders, filenames in os.walk(directory):
        for file in filenames:
            path = os.path.join(foldername, file)

            try:
                checksum = calculate_checksum(path)

                if checksum in files:
                    duplicates.append(path)
                else:
                    files[checksum] = path

            except Exception as e:
                print("Error:", e)

    return duplicates


def write_log(duplicates):
    with open("Log.txt", "w") as f:
        for file in duplicates:
            f.write(file + "\n")


def main():
    if len(sys.argv) != 2:
        print("Usage : DirectoryDuplicate.py DirectoryName")
        return

    directory = sys.argv[1]

    if not os.path.exists(directory):
        print("Directory not found")
        return

    duplicates = find_duplicates(directory)
    write_log(duplicates)


if __name__ == "__main__":
    main()