import os
from tkinter import messagebox

class UpdateFriend:

    @staticmethod
    def main(data):
        try:
            # Get the name of the contact to be updated from the command line arguments
            input_name = data[0]
            # Get the new number to be updated from the command line arguments
            new_number = int(data[1])
            
            file_path = "friendsContact.txt"

            # Create the file if it doesn't exist
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    pass

            found = False
            tmp_file_path = "temp.txt"

            # Open the original file and a temporary file for writing
            with open(file_path, 'r') as file, open(tmp_file_path, 'w') as tmp_file:
                for line in file:
                    line_split = line.strip().split("!")
                    if len(line_split) == 2:
                        name = line_split[0]
                        number = int(line_split[1])

                        # Check if the fetched contact is the one to be updated
                        if name == input_name:
                            # Update the number of this contact
                            line = f"{name}!{new_number}\n"
                            found = True

                    # Write the line (updated or not) to the temporary file
                    tmp_file.write(line)

            # If the contact has been updated, copy the temporary file back to the original
            if found:
                os.replace(tmp_file_path, file_path)
                messagebox.showinfo("Success", "Friend updated.")
            else:
                os.remove(tmp_file_path)  # Remove the temporary file if no updates were made
                messagebox.showwarning("Warning", "Friend not found.")

        except IOError as ioe:
            print(ioe)
        except ValueError as ve:
            print(ve)

# Example usage:
if __name__ == "__main__":
    import sys
    UpdateFriend.main(sys.argv[1:])
