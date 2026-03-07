import os
import sys
import zipfile
import shutil
from datetime import datetime
import smtplib
from email.message import EmailMessage

LOG_FOLDER = "Logs"
HISTORY_FILE = "backup_history.txt"

# Ignore extensions
IGNORE_EXT = ['.tmp', '.log', '.exe']


# Create Logs folder
def create_log_folder():
    if not os.path.exists(LOG_FOLDER):
        os.mkdir(LOG_FOLDER)


# Write log
def write_log(message):

    create_log_folder()

    log_file = os.path.join(LOG_FOLDER, "backup_log.txt")

    with open(log_file, "a") as f:
        f.write(message + "\n")


# Create ZIP backup
def create_backup(source):

    try:

        start_time = datetime.now()
        write_log(f"Backup Started : {start_time}")

        zip_name = "Backup_" + start_time.strftime("%Y%m%d_%H%M%S") + ".zip"

        zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

        file_count = 0

        for foldername, subfolders, filenames in os.walk(source):

            for file in filenames:

                ext = os.path.splitext(file)[1]

                if ext in IGNORE_EXT:
                    continue

                filepath = os.path.join(foldername, file)

                zipf.write(filepath)

                file_count += 1

        zipf.close()

        write_log(f"Files Copied : {file_count}")
        write_log(f"Zip File : {zip_name}")

        size = os.path.getsize(zip_name)

        update_history(file_count, size)

        return zip_name

    except Exception as e:
        write_log(f"Error : {str(e)}")


# Update Backup History
def update_history(files, size):

    with open(HISTORY_FILE, "a") as f:

        date = datetime.now()

        f.write(f"{date} | Files: {files} | Zip Size: {size}\n")


# Show history
def show_history():

    if not os.path.exists(HISTORY_FILE):
        print("No backup history found")
        return

    with open(HISTORY_FILE) as f:
        print(f.read())


# Restore backup
def restore_backup(zipfile_name, destination):

    try:

        with zipfile.ZipFile(zipfile_name, 'r') as zip_ref:

            zip_ref.extractall(destination)

        print("Restore completed")

    except Exception as e:
        print("Restore failed:", e)


# Send email
def send_email(receiver, zipfile_name):

    sender = "yourgmail@gmail.com"
    password = "your_app_password"

    msg = EmailMessage()

    msg['Subject'] = "Backup Completed"
    msg['From'] = sender
    msg['To'] = receiver

    msg.set_content("Backup completed successfully.")

    # Attach log
    log_file = os.path.join(LOG_FOLDER, "backup_log.txt")

    with open(log_file, "rb") as f:
        msg.add_attachment(f.read(),
                           maintype="application",
                           subtype="txt",
                           filename="backup_log.txt")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(sender, password)

        smtp.send_message(msg)


# Main function
def main():

    if len(sys.argv) < 2:
        print("Invalid arguments")
        return

    # Restore command
    if sys.argv[1] == "--restore":

        zipfile_name = sys.argv[2]
        destination = sys.argv[3]

        restore_backup(zipfile_name, destination)

    # History command
    elif sys.argv[1] == "--history":

        show_history()

    # Backup command
    else:

        source = sys.argv[1]
        email = sys.argv[2]

        zipfile_name = create_backup(source)

        send_email(email, zipfile_name)


if __name__ == "__main__":
    main()