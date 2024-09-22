import tkinter as tk

class Clear:
    def __init__(self, name_entry, number_entry):
        self.name_entry = name_entry
        self.number_entry = number_entry

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)
