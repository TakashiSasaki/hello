import tkinter as tk
from tkinter import filedialog
import os

class DragAndDropApp:
    def __init__(self, master):
        self.master = master
        master.title("Drag and Drop App")

        self.label = tk.Label(master, text="Drag and drop files here")
        self.label.pack(pady=20)

        self.listbox = tk.Listbox(master, width=50, height=10)
        self.listbox.pack(pady=20)

        self.label.drop_target_register(tk.DND_FILES)
        self.label.dnd_bind('<<Drop>>', self.drop)

    def drop(self, event):
        files = event.data
        if files:
            file_list = files.split("} {")
            for file in file_list:
                file = file.strip("{}")
                if os.path.isfile(file):
                    self.listbox.insert(tk.END, file)
                else:
                    print(f"Invalid file path: {file}")

root = tk.Tk()
app = DragAndDropApp(root)
root.mainloop()
