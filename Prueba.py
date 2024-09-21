import tkinter as tk
from tkinter import messagebox
import os

class FriendManager:
    def __init__(self, filename="friendsContact.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                pass  # Create the file if it doesn't exist

    def add_Friend(self, name, number):
        with open(self.filename, 'r+') as f:
            Friends = f.readlines()
            for Friend in Friends:
                if Friend.startswith(name) or Friend.split('!')[1].strip() == str(number):
                    return False  # Friend already exists
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
                    continue  # Skip the friend to delete
                f.write(Friend)
        return found

class App:
    def __init__(self, root):
        self.manager = FriendManager()

        # Create the main frame
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

        # Create a frame for buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        # Buttons
        button_style = {'width': 8, 'font': ('Arial', 9)}  # Size and font style
        self.create_button = tk.Button(self.button_frame, text="Create", command=lambda: self.perform_action("add"), **button_style)
        self.create_button.grid(row=0, column=0, padx=7)

        self.read_button = tk.Button(self.button_frame, text="Read", command=lambda: self.perform_action("read"), **button_style)
        self.read_button.grid(row=0, column=1, padx=7)

        self.update_button = tk.Button(self.button_frame, text="Update", command=lambda: self.perform_action("update"), **button_style)
        self.update_button.grid(row=0, column=2, padx=7)

        self.delete_button = tk.Button(self.button_frame, text="Delete", command=lambda: self.perform_action("delete"), **button_style)
        self.delete_button.grid(row=0, column=3, padx=7)

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_entries, **button_style)
        self.clear_button.grid(row=0, column=4, padx=7)

    def perform_action(self, action_type):
        name = self.name_entry.get()
        number = self.number_entry.get()
        
        if action_type == "add":
            success = self.manager.add_Friend(name, number)
            self.show_message("Friend added." if success else "Friend already exists.", success)
        elif action_type == "read":
            friends = self.manager.read_Friends()
            display = "".join(friends) if friends else "No friends found."
            messagebox.showinfo("Friends", display)
        elif action_type == "update":
            success = self.manager.update_Friend(name, number)
            self.show_message("Friend updated." if success else "Friend not found.", success)
        elif action_type == "delete":
            success = self.manager.delete_Friend(name)
            self.show_message("Friend deleted." if success else "Friend not found.", success)

    def show_message(self, message, success):
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showwarning("Warning", message)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Friends Manager")
    root.geometry("450x150")
    root.resizable(False, False)  # Restrict window size
    app = App(root)
    root.mainloop()
