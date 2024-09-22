import os
from tkinter import messagebox

class UpdateFriend:
    def __init__(self):
        pass

    def main(file_path, new_name, new_number):
        try:
            input_name = new_name.get()
            try:
                update_number = int(new_number.get())
            except ValueError:
                    messagebox.showwarning("Warning", "The number must be a valid integer.")
                    return

            found = False
            tmp_file_path = "temp.txt"

            with open(file_path, 'r') as file, open(tmp_file_path, 'w') as tmp_file:
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
                os.replace(tmp_file_path, file_path)
                messagebox.showinfo("Success", "Friend updated.")
            else:
                os.remove(tmp_file_path)
                messagebox.showwarning("Warning", "Friend not found.")

        except IOError as ioe:
            print(ioe)
        except ValueError as ve:
            print(ve)

