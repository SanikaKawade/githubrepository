# DirectoryRename.py

import os
import sys
import logging

def setup_logger():
    logging.basicConfig(filename="DirectoryRename.log",
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

def validate_inputs(directory, old_ext, new_ext):
    if not os.path.isdir(directory):
        raise FileNotFoundError("Directory does not exist.")
    if not old_ext.startswith(".") or not new_ext.startswith("."):
        raise ValueError("Extensions must start with '.'")

def rename_files(directory, old_ext, new_ext):
    for file in os.listdir(directory):
        if file.endswith(old_ext):
            base = file[:-len(old_ext)]
            new_name = base + new_ext
            os.rename(os.path.join(directory, file),
                      os.path.join(directory, new_name))
            logging.info(f"Renamed {file} to {new_name}")

def main():
    setup_logger()
    try:
        if len(sys.argv) != 4:
            raise ValueError("Usage: DirectoryRename.py <Directory> <OldExt> <NewExt>")

        directory = sys.argv[1]
        old_ext = sys.argv[2]
        new_ext = sys.argv[3]

        validate_inputs(directory, old_ext, new_ext)
        rename_files(directory, old_ext, new_ext)

    except Exception as e:
        logging.error(str(e))

if __name__ == "__main__":
    main()