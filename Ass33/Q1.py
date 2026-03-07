import psutil
import time
import os
import sys
import smtplib
from datetime import datetime
from email.message import EmailMessage


def create_log_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


def get_log_file(folder):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join(folder, f"Log_{timestamp}.txt")


def get_open_files_count(proc):
    try:
        return len(proc.open_files())
    except:
        return "Access Denied"


def collect_process_info():
    data = []

    for proc in psutil.process_iter(['pid','name','cpu_percent','memory_info','num_threads']):
        try:
            info = proc.info

            rss = info['memory_info'].rss

            open_files = get_open_files_count(proc)

            data.append({
                "name": info['name'],
                "pid": info['pid'],
                "cpu": info['cpu_percent'],
                "rss": rss,
                "threads": info['num_threads'],
                "open_files": open_files
            })

        except:
            pass

    return data


def write_log(file_path, processes):

    with open(file_path,"w") as f:

        for p in processes:

            f.write(f"Process Name : {p['name']}\n")
            f.write(f"PID : {p['pid']}\n")
            f.write(f"CPU % : {p['cpu']}\n")
            f.write(f"Memory (RSS) : {p['rss']}\n")
            f.write(f"Threads Count : {p['threads']}\n")
            f.write(f"Open Files Count : {p['open_files']}\n")
            f.write(f"Timestamp : {datetime.now()}\n")
            f.write("\n----------------------\n\n")


def send_email(receiver, logfile):

    sender = "yourgmail@gmail.com"
    password = "your_app_password"

    msg = EmailMessage()

    msg["Subject"] = "System Surveillance Report"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content("Attached is the system monitoring report.")

    with open(logfile,'rb') as f:
        file_data = f.read()

    msg.add_attachment(file_data,
                       maintype="application",
                       subtype="txt",
                       filename=os.path.basename(logfile))

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(sender,password)
        smtp.send_message(msg)


def surveillance(logfolder, receiver, interval):

    create_log_folder(logfolder)

    while True:

        logfile = get_log_file(logfolder)

        processes = collect_process_info()

        write_log(logfile, processes)

        print("Log created:", logfile)

        try:
            send_email(receiver, logfile)
            print("Email Sent")
        except:
            print("Email failed")

        time.sleep(interval * 60)


def main():

    if len(sys.argv) != 4:
        print("Usage: PlatformSurveillance.py LogFolder Email Interval")
        exit()

    logfolder = sys.argv[1]
    receiver = sys.argv[2]
    interval = int(sys.argv[3])

    surveillance(logfolder, receiver, interval)


if __name__ == "__main__":
    main()