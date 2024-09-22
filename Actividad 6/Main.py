import tkinter as tk
from tkinter import messagebox
import os

class FriendManager:
    def __init__(self, filename="friendsContact.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                pass  # Create the file if it doesn't exist

    def add_friend(self, name, number):
        with open(self.filename, 'r+') as f:
            friends = f.readlines()
            for friend in friends:
                if friend.split('!')[0].strip() == str(name) and friend.split('!')[1].strip() == str(number):
                    return False  # Friend already exists
            f.write(f"{name}!{number}\n")
        return True

    def read_friend(self, name):
        with open(self.filename, 'r') as f:
            for friend in f:
                if friend.split('!')[0].strip() == str(name):
                    return friend.split('!')[1].strip()  # Return the number
        return None  # Return None if not found

    def update_friend(self, name, new_number):
        found = False
        with open(self.filename, 'r') as f:
            friends = f.readlines()
        with open(self.filename, 'w') as f:
            for friend in friends:
                if friend.split('!')[0].strip() == str(name):
                    f.write(f"{name}!{new_number}\n")
                    found = True
                else:
                    f.write(friend)
        return found

    def delete_friend(self, name):
        found = False
        with open(self.filename, 'r') as f:
            friends = f.readlines()
        with open(self.filename, 'w') as f:
            for friend in friends:
                if friend.split('!')[0].strip() == str(name):
                    found = True
                    continue  # Skip the friend to delete
                f.write(friend)
        return found

class Create:
    def __init__(self, manager):
        self.manager = manager

    def add_friend(self, name, number):
        if self.manager.add_friend(name, number):
            messagebox.showinfo("Success", "Friend added.")
        else:
            messagebox.showwarning("Warning", "Friend already exists.")

class Read:
    def __init__(self, manager):
        self.manager = manager

    def get_friend(self, name):
        number = self.manager.read_friend(name)
        return number

class Update:
    def __init__(self, manager):
        self.manager = manager

    def update_friend(self, name, new_number):
        if self.manager.update_friend(name, new_number):
            messagebox.showinfo("Success", "Friend updated.")
        else:
            messagebox.showwarning("Warning", "Friend not found.")

class Delete:
    def __init__(self, manager):
        self.manager = manager

    def delete_friend(self, name):
        if self.manager.delete_friend(name):
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

        # Create instances of action classes
        self.create = Create(self.manager)
        self.read = Read(self.manager)
        self.update = Update(self.manager)
        self.delete = Delete(self.manager)

        # Create the main frame
        self.frame = tk.Frame(root, padx=10, pady=10)
        self.frame.pack(expand=True)

        # Labels and Entries
        self.name_label = tk.Label(self.frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=20, pady=5)
        self.name_entry = tk.Entry(self.frame, width=30)
        self.name_entry.grid(row=0, column=1, pady=5)

        self.number_label = tk.Label(self.frame, text="Number:")
        self.number_label.grid(row=1, column=0, padx=20)
        self.number_entry = tk.Entry(self.frame, width=30)
        self.number_entry.grid(row=1, column=1, pady=5)

        # Buttons
        self.create_button = tk.Button(self.frame, text="Create", command=self.add_friend)
        self.create_button.grid(row=2, column=0, padx=7)

        self.read_button = tk.Button(self.frame, text="Read", command=self.get_friend)
        self.read_button.grid(row=2, column=1, padx=7)

        self.update_button = tk.Button(self.frame, text="Update", command=self.update_friend)
        self.update_button.grid(row=2, column=2, padx=7)

        self.delete_button = tk.Button(self.frame, text="Delete", command=self.delete_friend)
        self.delete_button.grid(row=2, column=3, padx=7)

        self.clear_button = tk.Button(self.frame, text="Clear", command=self.clear_entries)
        self.clear_button.grid(row=2, column=4, padx=7)

    def add_friend(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        self.create.add_friend(name, number)
        self.clear_entries()  # Clear entries after adding

    def get_friend(self):
        name = self.name_entry.get()
        number = self.read.get_friend(name)
        if number:
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, number)  # Populate the number entry
        else:
            messagebox.showwarning("Warning", "Friend not found.")

    def update_friend(self):
        name = self.name_entry.get()
        new_number = self.number_entry.get()
        self.update.update_friend(name, new_number)
        self.clear_entries()  # Clear entries after updating

    def delete_friend(self):
        name = self.name_entry.get()
        self.delete.delete_friend(name)
        self.clear_entries()  # Clear entries after deleting

    def clear_entries(self):
        Clear(self.name_entry, self.number_entry).clear_entries()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Friendform")
    root.geometry("600x150")
    root.resizable(False, False)  # Restrict window size
    app = App(root)
    root.mainloop()
