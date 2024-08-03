import tkinter as tk
import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_discriminante(self):
        return math.pow(self.b, 2) - 4 * self.a * self.c

    def calcular_raices(self):
        discriminante = self.calcular_discriminante()
        if discriminante > 0:
            raiz1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return "X_1 = {:.2f}, X_2 = {:.2f}".format(raiz1, raiz2)
        elif discriminante == 0:
            raiz = -self.b / (2 * self.a)
            return "La única solución es: {:.2f}".format(raiz)
        else:
            return "No hay solución en los números reales"

def GUI():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        ecuacion = EcuacionCuadratica(a, b, c)
        resultado = ecuacion.calcular_raices()
        text_resultado.config(state=tk.NORMAL)
        text_resultado.delete("1.0", tk.END)
        text_resultado.insert(tk.END, resultado)
        text_resultado.config(state=tk.DISABLED)
    except ValueError:
        text_resultado.config(state=tk.NORMAL)
        text_resultado.delete("1.0", tk.END)
        text_resultado.insert(tk.END, "Error al ingresar los datos")
        text_resultado.config(state=tk.DISABLED)

def limpiar():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    text_resultado.config(state=tk.NORMAL)
    text_resultado.delete("1.0", tk.END)
    text_resultado.config(state=tk.DISABLED)

# Ventana principal
ventana = tk.Tk()
ventana.title("Solución ecuación cuadrática")

# Widgets de la GUI
label_a = tk.Label(ventana, text="Ingrese el coeficiente A: ")
label_a.grid(row=0, column=0, padx=10, pady=5)

entry_a = tk.Entry(ventana)
entry_a.grid(row=0, column=1, padx=10, pady=5)

label_b = tk.Label(ventana, text="Ingrese el coeficiente B: ")
label_b.grid(row=1, column=0, padx=10, pady=5)

entry_b = tk.Entry(ventana)
entry_b.grid(row=1, column=1, padx=10, pady=5)

label_c = tk.Label(ventana, text="Ingrese el coeficiente C: ")
label_c.grid(row=2, column=0, padx=10, pady=5)

entry_c = tk.Entry(ventana)
entry_c.grid(row=2, column=1, padx=10, pady=5)

boton_calcular = tk.Button(ventana, text="Calcular las raíces", command=GUI)
boton_calcular.grid(row=3, column=0, columnspan=1, pady=10)

text_resultado = tk.Text(ventana, width=25, height=2, state=tk.DISABLED)
text_resultado.grid(row=3, column=1, padx=10, pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=4, column=0, columnspan=2, pady=10)

# Bucle principal
ventana.mainloop()
