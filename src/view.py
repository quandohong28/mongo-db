# view.py
import tkinter as tk

class MongoDBView:
    def __init__(self, root):
        self.root = root
        self.root.title("MongoDB Control Panel")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.eval('tk::PlaceWindow . center')

        self.start_button = tk.Button(root, text="Start MongoDB")
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop MongoDB")
        self.stop_button.pack(pady=10)

        self.status_label = tk.Label(root, text="Status: Not started", fg="blue")
        self.status_label.pack(pady=10)

        self.log_text = tk.Text(root, wrap=tk.WORD, width=80, height=20)
        self.log_text.pack(pady=10, padx=10)

    def update_status(self, message):
        self.status_label.config(text=message)

    def append_log(self, message):
        self.log_text.insert(tk.END, message)
        self.log_text.yview(tk.END)
