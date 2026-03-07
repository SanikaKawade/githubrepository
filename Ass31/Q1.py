# DirectoryFileSearch.py

import os
import sys
import logging

def setup_logger():
    logging.basicConfig(filename="DirectoryFileSearch.log",
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

def validate_inputs(directory, extension):
    if not os.path.isdir(directory):
        raise FileNotFoundError("Directory does not exist.")
    if not extension.startswith("."):
        raise ValueError("Extension must start with '.'")

def search_files(directory, extension):
    files = [f for f in os.listdir(directory) if f.endswith(extension)]
    return files

def main():
    setup_logger()
    try:
        if len(sys.argv) != 3:
            raise ValueError("Usage: DirectoryFileSearch.py <Directory> <Extension>")

        directory = sys.argv[1]
        extension = sys.argv[2]

        validate_inputs(directory, extension)
        files = search_files(directory, extension)

        if files:
            logging.info("Files found:")
            for file in files:
                logging.info(file)
        else:
            logging.info("No files found with given extension.")

    except Exception as e:
        logging.error(str(e))

if __name__ == "__main__":
    main()