import os
from tkinter import messagebox

class DisplayFriends:

    @staticmethod
    def main():
        try:
            file_path = "friendsContact.txt"

            # Create the file if it doesn't exist
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    pass

            # Reading the file and displaying contacts
            with open(file_path, 'r') as file:
                found = False
                for line in file:
                    line_split = line.strip().split("!")
                    if len(line_split) == 2:  # Ensure there's a name and a number
                        name = line_split[0]
                        number = int(line_split[1])
                        
                        # Print the contact data
                        messagebox.showinfo("Success", f"Friend Name: {name}\nContact Number: {number}\n")
                        found = True
                
                if not found:
                    messagebox.showinfo("Friends", "No contacts found.")
                    
        except IOError as ioe:
            print(ioe)
        except ValueError as ve:
            print(ve)

# Example usage:
if __name__ == "__main__":
    DisplayFriends.main()
