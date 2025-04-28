import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading
import time
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'


MONGOD_PATH = "/usr/local/mongodb/bin/mongod"
MONGO_DB_PATH = "/usr/local/mongodb/data/db"

class MongodManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MongoDB Manager")

        self.status_label = tk.Label(root, text="Status: Unknown", font=("Arial", 14))
        self.status_label.pack(pady=5)

        self.version_label = tk.Label(root, text="Version: Unknown", font=("Arial", 14))
        self.version_label.pack(pady=5)

        self.port_label = tk.Label(root, text="Port: Unknown", font=("Arial", 14))
        self.port_label.pack(pady=5)

        port_frame = tk.Frame(root)
        port_frame.pack(pady=5)
        tk.Label(port_frame, text="Port:", font=("Arial", 12)).pack(side=tk.LEFT)
        self.port_entry = tk.Entry(port_frame, width=10)
        self.port_entry.insert(0, "27017")
        self.port_entry.pack(side=tk.LEFT)

        self.toggle_button = tk.Button(root, text="Start Mongod", command=self.toggle_mongod)
        self.toggle_button.pack(pady=5)

        self.refresh_button = tk.Button(root, text="Refresh", command=self.update_status)
        self.refresh_button.pack(pady=5)

        self.log_text = scrolledtext.ScrolledText(root, width=80, height=20, state='disabled')
        self.log_text.pack(pady=10)

        self.mongod_process = None

        self.update_status()
        threading.Thread(target=self.auto_update, daemon=True).start()

    def get_mongod_version(self):
        try:
            output = subprocess.check_output([MONGOD_PATH, "--version"]).decode()
            for line in output.splitlines():
                if "db version" in line:
                    return line.split(":")[1].strip()
        except:
            return "Unknown"

    def get_mongod_status(self):
        try:
            output = subprocess.check_output(["pgrep", "-f", "mongod"]).decode()
            return True if output.strip() else False
        except:
            return False

    def get_mongod_port(self):
        try:
            output = subprocess.check_output(["lsof", "-iTCP", "-sTCP:LISTEN", "-nP"]).decode()
            for line in output.splitlines():
                if "mongod" in line:
                    parts = line.split()
                    for part in parts:
                        if "TCP" in part:
                            port = part.split(":")[-1]
                            return port
            return "Unknown"
        except:
            return "Unknown"

    def start_mongod(self):
        port = self.port_entry.get().strip()

        cmd = [MONGOD_PATH, "--dbpath", MONGO_DB_PATH, "--port", port]
        try:
            self.mongod_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            threading.Thread(target=self.read_logs, daemon=True).start()
        except Exception as e:
            self.write_log(f"Failed to start mongod: {e}")

    def stop_mongod(self):
        try:
            subprocess.call(["pkill", "-f", "mongod"])
            self.write_log("Mongod stopped.")
        except Exception as e:
            self.write_log(f"Failed to stop mongod: {e}")

    def toggle_mongod(self):
        if self.get_mongod_status():
            self.stop_mongod()
            self.toggle_button.config(text="Start Mongod")
        else:
            self.start_mongod()
            self.toggle_button.config(text="Stop Mongod")

        self.update_status()

    def update_status(self):
        version = self.get_mongod_version()
        running = self.get_mongod_status()
        port = self.get_mongod_port() if running else "Not running"

        self.version_label.config(text=f"Version: {version}")
        self.status_label.config(text=f"Status: {'Running' if running else 'Stopped'}")
        self.port_label.config(text=f"Port: {port}")

        if running:
            self.toggle_button.config(text="Stop Mongod")
        else:
            self.toggle_button.config(text="Start Mongod")

    def auto_update(self):
        while True:
            self.update_status()
            time.sleep(5)

    def read_logs(self):
        if not self.mongod_process:
            return
        while True:
            line = self.mongod_process.stdout.readline()
            if not line:
                break
            self.write_log(line.strip())

    def write_log(self, text):
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, text + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = MongodManagerApp(root)
    root.resizable(False, False)
    root.mainloop()