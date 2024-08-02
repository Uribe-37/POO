import tkinter as tk

class NumMayor():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def mayor(self):
        if self.num1 > self.num2:
            return "{} es mayor que {}".format(self.num1, self.num2)
        elif self.num1 == self.num2:
            return "{} es igual a {}".format(self.num1, self.num2)
        else:
            return "{} es mayor que {}".format(self.num2, self.num1)

    def __str__(self):
        return "{}".format(self.mayor())

def calcular_mayor():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        num_mayor = NumMayor(num1, num2)
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, str(num_mayor))
    except ValueError:
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error: Por favor, ingrese números válidos")

def limpiar_campos():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    entry_resultado.config(state=tk.NORMAL)
    entry_resultado.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Número mayor")

# Crear y colocar los widgets usando grid para una mejor organización
label_num1 = tk.Label(ventana, text="Ingrese el primer número:")
label_num1.grid(row=0, column=0, padx=10, pady=5)

entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(ventana, text="Ingrese el segundo número:")
label_num2.grid(row=1, column=0, padx=10, pady=5)

entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

boton_calcular = tk.Button(ventana, text="Obtener el número mayor", command=calcular_mayor)
boton_calcular.grid(row=2, column=0, columnspan=1, pady=10)

entry_resultado = tk.Entry(ventana)
entry_resultado.grid(row=2, column=1, padx=10, pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
boton_limpiar.grid(row=3, column=0, columnspan=2, pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
