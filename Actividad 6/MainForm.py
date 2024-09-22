import os
import tkinter as tk
from tkinter import messagebox

class Friends:
    def __init__(self):
        pass

    def main(self):
        self.main_form = MainForm(tk.Tk())

class MainForm:
    def __init__(self, root):
        self.file_path = "friendsContact.txt"

        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                pass

        root.title("Friends")
        root.geometry("450x150")
        root.resizable(False, False)  # Window size cannot be changed

        # Frame for the form
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

        # Button Frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        # Buttons
        button_style = {'width': 8, 'font': ('Arial', 9)}
        self.create_button = tk.Button(self.button_frame, text="Create", command=self.Create, **button_style)
        self.create_button.grid(row=0, column=0, padx=7)

        self.read_button = tk.Button(self.button_frame, text="Read", command=self.Read, **button_style)
        self.read_button.grid(row=0, column=1, padx=7)

        self.update_button = tk.Button(self.button_frame, text="Update", command=self.Update, **button_style)
        self.update_button.grid(row=0, column=2, padx=7)

        self.delete_button = tk.Button(self.button_frame, text="Delete", command=self.Delete, **button_style)
        self.delete_button.grid(row=0, column=3, padx=7)

        # Clear Button
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.Clear, **button_style)
        self.clear_button.grid(row=0, column=4, padx=7)

        # Start the main loop
        root.mainloop()

    def Create(self):
        if not self.name_entry.get() or not self.number_entry.get():
            messagebox.showwarning("Warning", "Both fields are required.")
            return
        
        try:
            nuevo_name = self.name_entry.get()
            try:
                nuevo_number = int(self.number_entry.get())
            except ValueError:
                messagebox.showwarning("Warning", "The number must be a valid integer.")
                return

            found = False
            
            with open(self.file_path, 'r+') as file:
                for line in file:
                    line_split = line.strip().split("!")
                    name = line_split[0]
                    number = int(line_split[1])

                    if name == nuevo_name and number == nuevo_number:
                        found = True
                        break
                
                if not found:
                    file.write(f"{nuevo_name}!{nuevo_number}\n")
                    messagebox.showinfo("Success", "Friend added.")
                else:
                    messagebox.showwarning("Warning", "Friend already exists.")

        except IOError as ioe:
            print(ioe)

    def Read(self):
        try:
            input_name = self.name_entry.get()

            with open(self.file_path, 'r') as file:
                found = False
                for line in file:
                    line_split = line.strip().split("!")
                    if len(line_split) == 2:
                        name = line_split[0]
                        number = int(line_split[1])

                        if name == input_name:
                            messagebox.showinfo("Success", f"Friend Name: {name}\nContact Number: {number}\n")
                            self.number_entry.delete(0, 'end')
                            self.number_entry.insert(0, str(number))
                            found = True
                            break

                if not found:
                    messagebox.showwarning("Warning", "Friend not found.")

        except IOError as ioe:
            print(ioe)
        except ValueError as ve:
            print(ve)

    def Update(self):
        try:
            input_name = self.name_entry.get()
            try:
                update_number = int(self.number_entry.get())
            except ValueError:
                messagebox.showwarning("Warning", "The number must be a valid integer.")
                return

            found = False
            tmp_file_path = "temp.txt"

            with open(self.file_path, 'r') as file, open(tmp_file_path, 'w') as tmp_file:
                for line in file:
                    line_split = line.strip().split("!")
                    if len(line_split) == 2:
                        name = line_split[0]
                        number = int(line_split[1])

                        if name == input_name:
                            line = f"{name}!{update_number}\n"
                            found = True

                    tmp_file.write(line)

            if found:
                os.replace(tmp_file_path, self.file_path)
                messagebox.showinfo("Success", "Friend updated.")
            else:
                os.remove(tmp_file_path)
                messagebox.showwarning("Warning", "Friend not found.")

        except IOError as ioe:
            print(ioe)
        except ValueError as ve:
            print(ve)

    def Delete(self):
        if not self.name_entry.get() or not self.number_entry.get():
            messagebox.showwarning("Warning", "Both fields are required.")
            return
        
        try:
            input_new_name = self.name_entry.get()
            try:
                input_new_number = int(self.number_entry.get())
            except ValueError:
                messagebox.showwarning("Warning", "The number must be a valid integer.")
                return

            found = False
            tmp_file_path = "temp.txt"

            with open(self.file_path, 'r') as file, open(tmp_file_path, 'w') as tmp_file:
                for line in file:
                    line_split = line.strip().split("!")
                    if len(line_split) == 2:
                        name = line_split[0]
                        number = int(line_split[1])

                        if name == input_new_name and number == input_new_number:
                            found = True
                            continue

                    tmp_file.write(line)

            if found:
                os.replace(tmp_file_path, self.file_path)
                messagebox.showinfo("Success", "Friend deleted.")
            else:
                os.remove(tmp_file_path)
                messagebox.showwarning("Warning", "Friend not found.")

        except IOError as ioe:
            print(ioe)

    def Clear(self):
        self.name_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)


if __name__ == "__main__":
    friends_app = Friends().main()
