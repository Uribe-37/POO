import os
import tkinter as tk
from Clear import Clear
from Create import CreateFriend
 

class FriendManager:
    def __init__(self, file_path="friendsContact.txt"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                pass

class App:
    def __init__(self, root):
        self.manager = FriendManager()

        # Crear el marco principal
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

        # Crear un marco para los botones
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        # Buttons
        button_style = {'width': 8, 'font': ('Arial', 9)}  # Tamaño y estilo de fuente
        self.create_button = tk.Button(self.button_frame, text="Create", command=CreateFriend(self.name_entry, self.number_entry).main, **button_style)
        self.create_button.grid(row=0, column=0, padx=7)

        self.read_button = tk.Button(self.button_frame, text="Read", **button_style)
        self.read_button.grid(row=0, column=1, padx=7)

        self.update_button = tk.Button(self.button_frame, text="Update", **button_style)
        self.update_button.grid(row=0, column=2, padx=7)

        self.delete_button = tk.Button(self.button_frame, text="Delete", **button_style)
        self.delete_button.grid(row=0, column=3, padx=7)

        # Aquí se crea una instancia de Clear y se pasa el método sin llamarlo
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=Clear(self.name_entry, self.number_entry).clear_entries, **button_style)
        self.clear_button.grid(row=0, column=4, padx=7)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Friends Manager")
    root.geometry("450x150")
    root.resizable(False, False)  # Restringir el tamaño de la ventana
    app = App(root)
    root.mainloop()
