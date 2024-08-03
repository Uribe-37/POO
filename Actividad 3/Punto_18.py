import tkinter as tk

class Empleado(object):
    def __init__(self, cod_empleado, nombre, num_horas_tra,Val_hora,porc_retencion):
        self.cod_empleado = cod_empleado
        self.nombre = nombre
        self.num_horas_tra = num_horas_tra
        self.Val_hora = Val_hora
        self.porc_retencion = porc_retencion
    
    def salario_bruto(self):
        return self.num_horas_tra * self.Val_hora
    
    def salario_neto(self):
        return self.salario_bruto() * (1 - self.porc_retencion / 100)
    
    def __str__(self):
        return "Codigo: {} - Nombre: {} - Salario Bruto: ${} - Salario Neto: ${}".format(self.cod_empleado,self.nombre, self.salario_bruto(),self.salario_neto())

def GUI():
    try:
        Cod = entry_cod.get()
        Nom = entry_nom.get()
        Horas = float(entry_horas.get())
        Valor = float(entry_valor.get())
        Ret = float(entry_ret.get())
        Empleado1 = Empleado(Cod, Nom, Horas, Valor, Ret)
        resultado.config(text = str(Empleado1))
    except ValueError:
        resultado.config(text="Error al ingresar los datos")

def limpiar():
    entry_cod.delete(0, tk.END)
    entry_nom.delete(0, tk.END)
    entry_horas.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    entry_ret.delete(0, tk.END)
    resultado.config(text="")

# Ventana principal
ventana = tk.Tk()
ventana.title("Salario de un empleado")

# Widgets de la GUI
label_cod = tk.Label(ventana, text="Ingrese el código del empleado: ")
label_cod.grid(row=0, column=0, padx=10, pady=5)

entry_cod = tk.Entry(ventana)
entry_cod.grid(row=0, column=1, padx=10, pady=5)

label_nom = tk.Label(ventana, text="Ingrese el nombre del empleado: ")
label_nom.grid(row=1, column=0, padx=10, pady=5)

entry_nom = tk.Entry(ventana)
entry_nom.grid(row=1, column=1, padx=10, pady=5)

label_horas = tk.Label(ventana, text="Ingrese el número de horas trabajadas: ")
label_horas.grid(row=2, column=0, padx=10, pady=5)

entry_horas = tk.Entry(ventana)
entry_horas.grid(row=2, column=1, padx=10, pady=5)

label_valor = tk.Label(ventana, text="Ingrese el valor de la hora: ")
label_valor.grid(row=3, column=0, padx=10, pady=5)

entry_valor = tk.Entry(ventana)
entry_valor.grid(row=3, column=1, padx=10, pady=5)

label_ret = tk.Label(ventana, text="Ingrese el porcentaje de retención: ")
label_ret.grid(row=4, column=0, padx=10, pady=5)

entry_ret = tk.Entry(ventana)
entry_ret.grid(row=4, column=1, padx=10, pady=5)

boton_calcular = tk.Button(ventana, text="Calcular el salario", command=GUI)
boton_calcular.grid(row=5, column=0, columnspan=1, pady=10)

resultado = tk.Label(ventana)
resultado.grid(row=5, column=1, padx=10, pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=6, column=0, columnspan=2, pady=10)

# Bucle principal
ventana.mainloop()



