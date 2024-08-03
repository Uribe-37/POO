import tkinter as tk

class Empleado:
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_por_hora * self.horas_trabajadas

    def comentario_salario(self):
        salario_mensual = self.calcular_salario_mensual()
        if salario_mensual > 450000:
            return "{}: {}".format(self.nombre, salario_mensual)
        else:
            return self.nombre

def GUI():
    try:
        nombre = entry_nombre.get()
        salario_por_hora = float(entry_salario_hora.get())
        horas_trabajadas = float(entry_horas.get())
        empleado = Empleado(nombre, salario_por_hora, horas_trabajadas)
        text_resultado.config(state=tk.NORMAL)
        text_resultado.delete("1.0", tk.END)
        text_resultado.insert(tk.END, empleado.comentario_salario())
        text_resultado.config(state=tk.DISABLED)
    except ValueError:
        text_resultado.config(state=tk.NORMAL)
        text_resultado.delete("1.0", tk.END)
        text_resultado.insert(tk.END, "Error al ingresar los datos")
        text_resultado.config(state=tk.DISABLED)

def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_salario_hora.delete(0, tk.END)
    entry_horas.delete(0, tk.END)
    text_resultado.config(state=tk.NORMAL)
    text_resultado.delete("1.0", tk.END)
    text_resultado.config(state=tk.DISABLED)

# Ventana principal
ventana = tk.Tk()
ventana.title("Salario mensual")

# Widgets de la GUI
label_nombre = tk.Label(ventana, text="Ingrese el nombre del empleado: ")
label_nombre.grid(row=0, column=0, padx=10, pady=5)

entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_salario_hora = tk.Label(ventana, text="Ingrese el salario por hora del empleado: ")
label_salario_hora.grid(row=1, column=0, padx=10, pady=5)

entry_salario_hora = tk.Entry(ventana)
entry_salario_hora.grid(row=1, column=1, padx=10, pady=5)

label_horas = tk.Label(ventana, text="Ingrese el número de horas trabajadas en el mes: ")
label_horas.grid(row=2, column=0, padx=10, pady=5)

entry_horas = tk.Entry(ventana)
entry_horas.grid(row=2, column=1, padx=10, pady=5)

boton_calcular = tk.Button(ventana, text="Calcular el salario mensual", command=GUI)
boton_calcular.grid(row=3, column=0, pady=10)

text_resultado = tk.Text(ventana, height=2, width=20, state=tk.DISABLED)
text_resultado.grid(row=3, column=1, padx=10, pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=4, column=0, columnspan=2, pady=10)

# Bucle principal
ventana.mainloop()
