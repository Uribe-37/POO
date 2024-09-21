import tkinter as tk
from tkinter import messagebox
import os

class FriendManager:
    def __init__(self, filename="friendsContact.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                pass  # Crea el archivo si no existe

    def add_Friend(self, name, number):
        with open(self.filename, 'r+') as f:
            Friends = f.readlines()
            for Friend in Friends:
                if Friend.startswith(name) or Friend.split('!')[1].strip() == str(number):
                    return False  # El Friend ya existe
            f.write(f"{name}!{number}\n")
        return True

    def read_Friends(self):
        with open(self.filename, 'r') as f:
            return f.readlines()

    def update_Friend(self, name, new_number):
        Friends = self.read_Friends()
        found = False
        with open(self.filename, 'w') as f:
            for Friend in Friends:
                if Friend.startswith(name):
                    f.write(f"{name}!{new_number}\n")
                    found = True
                else:
                    f.write(Friend)
        return found

    def delete_Friend(self, name):
        Friends = self.read_Friends()
        found = False
        with open(self.filename, 'w') as f:
            for Friend in Friends:
                if Friend.startswith(name):
                    found = True
                    continue  # Salta el Friend a eliminar
                f.write(Friend)

        if self.manager.delete_Friend(name):
            messagebox.showinfo("Success", "Friend deleted.")
        else:
            messagebox.showwarning("Warning", "Friend not found.")


        return found

class Create:
    def __init__(self, manager):
        self.manager = manager

    def add_Friend(self, name, number):
        if self.manager.add_Friend(name, number):
            messagebox.showinfo("Success", "Friend added.")
        else:
            messagebox.showwarning("Warning", "Friend already exists.")

class Read:
    def __init__(self, manager):
        self.manager = manager

    def display_Friends(self):
        Friends = self.manager.read_Friends()
        display = "".join(Friends)
        messagebox.showinfo("Friends", display if display else "No Friends found.")

class Update:
    def __init__(self, manager):
        self.manager = manager

    def update_Friend(self, name, new_number):
        if self.manager.update_Friend(name, new_number):
            messagebox.showinfo("Success", "Friend updated.")
        else:
            messagebox.showwarning("Warning", "Friend not found.")

class Delete:
    def __init__(self, manager):
        self.manager = manager

    def delete_Friend(self, name):
        if self.manager.delete_Friend(name):
            messagebox.showinfo("Success", "Friend deleted.")
        else:
            messagebox.showwarning("Warning", "Friend not found.")

class Clear:
    def __init__(self, name_entry, number_entry):
        self.name_entry = name_entry
        self.number_entry = number_entry

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)

class App:
    def __init__(self, root):
        self.manager = FriendManager()

        # Crear instancias de las clases de acciones
        self.create = Create(self.manager)
        self.read = Read(self.manager)
        self.update = Update(self.manager)
        self.delete = Delete(self.manager)

        # Crear el marco principal
        self.frame = tk.Frame(root, padx=10, pady=10)
        self.frame.pack(expand=True)

        # Labels and Entries
        self.name_label = tk.Label(self.frame, text="Name:", font=("Arial", 10, "bold"))
        self.name_label.grid(row=0, column=0, padx=20, pady=5)
        self.name_entry = tk.Entry(self.frame, width=30)
        self.name_entry.grid(row=0, column=1, pady=5)

        self.number_label = tk.Label(self.frame, text="Number:", font=("Arial", 10, "bold"))
        self.number_label.grid(row=1, column=0, padx=20)
        self.number_entry = tk.Entry(self.frame, width=30)
        self.number_entry.grid(row=1, column=1, pady=5)

        # Crear un marco para los botones
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        # Buttons
        button_style = {'width': 8, 'font': ('Arial', 9)}  # Tamaño y estilo de fuente
        self.create_button = tk.Button(self.button_frame, text="Create", command=self.add_Friend, **button_style)
        self.create_button.grid(row=0, column=0, padx=7)

        self.read_button = tk.Button(self.button_frame, text="Read", command=self.display_Friends, **button_style)
        self.read_button.grid(row=0, column=1, padx=7)

        self.update_button = tk.Button(self.button_frame, text="Update", command=self.update_Friend, **button_style)
        self.update_button.grid(row=0, column=2, padx=7)

        self.delete_button = tk.Button(self.button_frame, text="Delete", command=self.delete_Friend, **button_style)
        self.delete_button.grid(row=0, column=3, padx=7)

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_entries, **button_style)
        self.clear_button.grid(row=0, column=4, padx=7)

    def add_Friend(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        self.create.add_Friend(name, number)

    def display_Friends(self):
        self.read.display_Friends()

    def update_Friend(self):
        name = self.name_entry.get()
        new_number = self.number_entry.get()
        self.update.update_Friend(name, new_number)

    def delete_Friend(self):
        name = self.name_entry.get()
        self.delete.delete_Friend(name)

    def clear_entries(self):
        Clear(self.name_entry, self.number_entry).clear_entries()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Friends Manager")
    root.geometry("450x150")
    root.resizable(False, False)  # Restringir el tamaño de la ventana
    app = App(root)
    root.mainloop()

