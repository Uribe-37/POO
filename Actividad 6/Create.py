import os
from tkinter import messagebox

class CreateFriend:
    def __init__(self, name_entry, number_entry):
        self.name_entry = name_entry
        self.number_entry = number_entry

    @staticmethod
    def main():
        try:
            # Get the name of the contact to be added
            new_name = 'Juan'
            # Get the number to be added
            new_number = 124
            
            file_path = "friendsContact.txt"
            found = False
            
            # Create the file if it doesn't exist
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    pass
            
            # Reading the file and checking for existing contact
            with open(file_path, 'r+') as file:
                for line in file:
                    line_split = line.strip().split("!")
                    name = line_split[0]
                    number = int(line_split[1])

                    if name == new_name and number == new_number:
                        found = True
                        break
                
                if not found:
                    # Move the file pointer to the end of the file before writing
                    file.write(f"{new_name}!{new_number}\n")
                    messagebox.showinfo("Success", "Friend added.")
                else:
                    messagebox.showwarning("Warning", "Friend already exists.")

        except IOError as ioe:
            print(ioe)
        except ValueError as ve:
            print(ve)

