# DirectoryCopyExt.py

import os
import sys
import shutil
import logging

def setup_logger():
    logging.basicConfig(filename="DirectoryCopyExt.log",
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

def validate_inputs(src, ext):
    if not os.path.isdir(src):
        raise FileNotFoundError("Source directory does not exist.")
    if not ext.startswith("."):
        raise ValueError("Extension must start with '.'")

def copy_files_with_ext(src, dest, ext):
    if not os.path.exists(dest):
        os.mkdir(dest)
        logging.info("Destination directory created.")

    for file in os.listdir(src):
        if file.endswith(ext):
            shutil.copy(os.path.join(src, file), dest)
            logging.info(f"Copied {file}")

def main():
    setup_logger()
    try:
        if len(sys.argv) != 4:
            raise ValueError("Usage: DirectoryCopyExt.py <SourceDir> <DestDir> <Extension>")

        src = sys.argv[1]
        dest = sys.argv[2]
        ext = sys.argv[3]

        validate_inputs(src, ext)
        copy_files_with_ext(src, dest, ext)

    except Exception as e:
        logging.error(str(e))

if __name__ == "__main__":
    main()