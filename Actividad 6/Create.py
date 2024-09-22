from tkinter import messagebox

class CreateFriend:
    def __init__(self):
        pass

    def main(file_path, new_name, new_number):
        if not new_name.get() or not new_number.get():
            messagebox.showwarning("Warning", "Both fields are required.")
            return
        
        try:
            nuevo_name = new_name.get()
            try:
                nuevo_number = int(new_number.get())
            except ValueError:
                messagebox.showwarning("Warning", "The number must be a valid integer.")
                return

            found = False
            
            with open(file_path, 'r+') as file:
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
