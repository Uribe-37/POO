import os
from tkinter import messagebox

class DeleteFriend:
    def __init__(self):
        pass

    def main(file_path, new_name, new_number):
        # Verificar que ambos campos no estén vacíos
        if not new_name.get() or not new_number.get():
            messagebox.showwarning("Warning", "Both fields are required.")
            return
        
        try:
            input_new_name = new_name.get()
            # Intentar convertir new_number a entero
            try:
                input_new_number = int(new_number.get())
            except ValueError:
                messagebox.showwarning("Warning", "The number must be a valid integer.")
                return

            found = False
            tmp_file_path = "temp.txt"

            # Open the original file and a temporary file for writing
            with open(file_path, 'r') as file, open(tmp_file_path, 'w') as tmp_file:
                for line in file:
                    line_split = line.strip().split("!")
                    if len(line_split) == 2:
                        name = line_split[0]
                        number = int(line_split[1])

                        # Check if the fetched contact is the one to be deleted
                        if name == input_new_name and number == input_new_number:
                            found = True
                            continue  # Skip this contact

                    # Write the line (if it's not deleted) to the temporary file
                    tmp_file.write(line)

            # If the contact has been deleted, copy the temporary file back to the original
            if found:
                os.replace(tmp_file_path, file_path)
                messagebox.showinfo("Success", "Friend deleted.")
            else:
                os.remove(tmp_file_path)  # Remove the temporary file if no deletions were made
                messagebox.showwarning("Warning", "Friend not found.")

        except IOError as ioe:
            print(ioe)
