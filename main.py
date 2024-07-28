import tkinter as tk
import threading
from subprocess import Popen, PIPE
import os

# Suppress Tk Deprecation Warning
os.environ['TK_SILENCE_DEPRECATION'] = '1'

def run_mongod():
    process = Popen(['mongod', '--dbpath', '/usr/local/mongodb/data/db'], stdout=PIPE, stderr=PIPE, text=True)

    for line in iter(process.stdout.readline, ''):
        if "waiting for connections on port" in line:
            display_status("MongoDB started successfully")
        log_text.insert(tk.END, line)
        log_text.yview(tk.END)
    
    process.stdout.close()
    process.wait()

def display_status(message):
    status_label.config(text=message)

def start_mongod():
    display_status("Starting MongoDB...")
    threading.Thread(target=run_mongod).start()

def stop_mongod():
    process = Popen(['pkill', 'mongod'], stdout=PIPE, stderr=PIPE, text=True)
    for line in iter(process.stdout.readline, ''):
        log_text.insert(tk.END, line)
        log_text.yview(tk.END)
    process.stdout.close()
    process.wait()
    display_status("MongoDB stopped")

root = tk.Tk()
root.title("MongoDB Control Panel")
root.geometry("600x400")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')

start_button = tk.Button(root, text="Start MongoDB", command=start_mongod)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop MongoDB", command=stop_mongod)
stop_button.pack(pady=10)

status_label = tk.Label(root, text="Status: Not started", fg="blue")
status_label.pack(pady=10)

log_text = tk.Text(root, wrap=tk.WORD, width=80, height=20)
log_text.pack(pady=10, padx=10)

root.mainloop()
