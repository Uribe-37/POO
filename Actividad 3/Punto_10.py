import tkinter as tk

class PagoMatricula():
    def __init__(self,Ni,Nombres,Patrimonio,Estrato):
        self.Ni = Ni
        self.Nombres = Nombres
        self.Patrimonio = Patrimonio
        self.Estrato = Estrato
    
    def Matricula(self):
        Pago_matricula = 50000
        if self.Patrimonio > 2000000 and self.Estrato>3:
            Pago_matricula = Pago_matricula + 0.03*self.Patrimonio
        return "El estudiante con número de inscripción {} y nombres {} debe pagar $ {}".format(self.Ni,self.Nombres,Pago_matricula)
    
def GUI():
    try:
        Ni = int(entry_num1.get())
        Nombres = entry_nombre.get()
        Patrimonio = float(entry_patri.get())
        Estrato = int(entry_estrato.get())
        Estudiante = PagoMatricula(Ni,Nombres,Patrimonio,Estrato).Matricula()
        resultado.config(text = str(Estudiante))
    except ValueError:
        resultado.config(text="Error al ingresar los datos")

def limpiar():
    entry_num1.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_patri.delete(0, tk.END)
    entry_estrato.delete(0, tk.END)
    resultado.config(text="")

# Ventana principal
ventana = tk.Tk()
ventana.title("Pago de la matrícula")

# Widgets de la GUI
label_num1 = tk.Label(ventana, text="Ingrese el número de inscripción del estudiante: ")
label_num1.grid(row=0, column=0, padx=10, pady=5)

entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_nombre = tk.Label(ventana, text="Ingrese los nombres del estudiante: ")
label_nombre.grid(row=1, column=0, padx=10, pady=5)

entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)

label_patri = tk.Label(ventana, text="Ingrese el patrimonio del estudiante: ")
label_patri.grid(row=2, column=0, padx=10, pady=5)

entry_patri = tk.Entry(ventana)
entry_patri.grid(row=2, column=1, padx=10, pady=5)

label_estrato = tk.Label(ventana, text="Ingrese el estrato del estudiante: ")
label_estrato.grid(row=3, column=0, padx=10, pady=5)   

entry_estrato = tk.Entry(ventana)
entry_estrato.grid(row=3, column=1, padx=10, pady=5)

boton_calcular = tk.Button(ventana, text="Calcular el pago de la matrícula", command=GUI)
boton_calcular.grid(row=4, column=0, columnspan=1, pady=10)

resultado = tk.Label(ventana)
resultado.grid(row=4, column=1, padx=10, pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=5, column=0, columnspan=2, pady=10)

# Bucle principal
ventana.mainloop()
