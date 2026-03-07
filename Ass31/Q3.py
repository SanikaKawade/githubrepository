# DirectoryCopy.py

import os
import sys
import shutil
import logging

def setup_logger():
    logging.basicConfig(filename="DirectoryCopy.log",
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

def validate_inputs(src):
    if not os.path.isdir(src):
        raise FileNotFoundError("Source directory does not exist.")

def copy_files(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
        logging.info("Destination directory created.")

    for file in os.listdir(src):
        full_path = os.path.join(src, file)
        if os.path.isfile(full_path):
            shutil.copy(full_path, dest)
            logging.info(f"Copied {file}")

def main():
    setup_logger()
    try:
        if len(sys.argv) != 3:
            raise ValueError("Usage: DirectoryCopy.py <SourceDir> <DestDir>")

        src = sys.argv[1]
        dest = sys.argv[2]

        validate_inputs(src)
        copy_files(src, dest)

    except Exception as e:
        logging.error(str(e))

if __name__ == "__main__":
    main()