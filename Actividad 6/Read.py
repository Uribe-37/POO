from tkinter import messagebox

class ReadFriend:
    def __init__(self):
        pass

    def main(file_path, new_name, number_entry):

        try:
            input_name = new_name.get()

            with open(file_path, 'r') as file:
                found = False
                for line in file:
                    line_split = line.strip().split("!")
                    if len(line_split) == 2:
                        name = line_split[0]
                        number = int(line_split[1])

                        if name == input_name:
                            messagebox.showinfo("Success", f"Friend Name: {name}\nContact Number: {number}\n")
                            number_entry.delete(0, 'end')
                            number_entry.insert(0, str(number))
                            found = True
                            break

                if not found:
                    messagebox.showwarning("Warning", "Friend not found.")

        except IOError as ioe:
            print(ioe)
        except ValueError as ve:
            print(ve)
