import os
from tkinter import messagebox

class DeleteFriend:

    @staticmethod
    def main(data):
        try:
            # Get the name of the contact to be deleted from the command line arguments
            input_name = data[0]

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

                        # Check if the fetched contact is the one to be deleted
                        if name == input_name:
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

# Example usage:
if __name__ == "__main__":
    import sys
    DeleteFriend.main(sys.argv[1:])
