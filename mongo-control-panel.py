import tkinter as tk
from src.controller import MongoDBController

def main():
    root = tk.Tk()
    app = MongoDBController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
