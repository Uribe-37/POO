from tkinter import messagebox

class ReadFriend:
    def __init__(self):
        pass

    def main(file_path, new_name, number_entry):

        try:
            input_name = new_name.get()

            # Leer el archivo y mostrar contactos
            with open(file_path, 'r') as file:
                found = False
                for line in file:
                    line_split = line.strip().split("!")
                    if len(line_split) == 2:  # Asegurarse de que haya un nombre y un número
                        name = line_split[0]
                        number = int(line_split[1])

                        # Verificar si el contacto encontrado es el que se desea
                        if name == input_name:
                            # Mostrar la información del contacto
                            messagebox.showinfo("Success", f"Friend Name: {name}\nContact Number: {number}\n")
                            number_entry.delete(0, 'end')  # Limpiar el campo de número
                            number_entry.insert(0, str(number))  # Insertar el número encontrado
                            found = True

                if not found:
                    messagebox.showwarning("Warning", "Friend not found.")

        except IOError as ioe:
            print(ioe)
        except ValueError as ve:
            print(ve)
