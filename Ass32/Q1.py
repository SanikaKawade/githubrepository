import os
import sys
import hashlib

def calculate_checksum(file_path):
    hash_obj = hashlib.md5()

    try:
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                hash_obj.update(chunk)

        return hash_obj.hexdigest()

    except Exception as e:
        return f"Error : {e}"


def directory_checksum(directory):
    if not os.path.exists(directory):
        print("Directory does not exist")
        return

    for foldername, subfolders, filenames in os.walk(directory):
        for file in filenames:
            path = os.path.join(foldername, file)
            checksum = calculate_checksum(path)
            print(f"{file} -> {checksum}")


def main():
    if len(sys.argv) != 2:
        print("Usage : DirectoryChecksum.py DirectoryName")
        return

    directory = sys.argv[1]
    directory_checksum(directory)


if __name__ == "__main__":
    main()