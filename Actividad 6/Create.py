import os
from tkinter import messagebox

class CreateFriend:
    def __init__(self):
        pass

    def main(file_path, new_name, new_number):
        try:
            nuevo_name = new_name.get()
            nuevo_number = int(new_number.get())

            found = False
            
            # Reading the file and checking for existing contact
            with open(file_path, 'r+') as file:
                for line in file:
                    line_split = line.strip().split("!")
                    name = line_split[0]
                    number = int(line_split[1])

                    if name == nuevo_name and number == nuevo_number:
                        found = True
                        break
                
                if not found:
                    # Move the file pointer to the end of the file before writing
                    file.write(f"{nuevo_name}!{nuevo_number}\n")
                    messagebox.showinfo("Success", "Friend added.")
                else:
                    messagebox.showwarning("Warning", "Friend already exists.")

        except IOError as ioe:
            print(ioe)
        except ValueError as ve:
            print(ve)

