import tkinter as tk

class TrianguloEquilatero(object):
    
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return (self.lado ** 2) * (3 ** 0.5) / 4

    def perimetro(self):
        return self.lado * 3
    
    def altura(self):
        return (self.lado * (3 ** 0.5)) / 2

def GUI():
    try:
        
        Triangulo1 = TrianguloEquilatero(Lado)
        resultado_area.delete(0, tk.END)
        resultado_area.insert(0, str(Triangulo1.area()))
        resultado_perimetro.delete(0, tk.END)
        resultado_perimetro.insert(0, str(Triangulo1.perimetro()))
        resultado_altura.delete(0, tk.END)
        resultado_altura.insert(0, str(Triangulo1.altura()))
    except ValueError:
        resultado_area.delete(0, tk.END)
        resultado_area.insert(0, "Error: Por favor, ingrese un número válido")
        resultado_perimetro.delete(0, tk.END)
        resultado_perimetro.insert(0, "Error: Por favor, ingrese un número válido")
        resultado_altura.delete(0, tk.END)
        resultado_altura.insert(0, "Error: Por favor, ingrese un número válido")

def limpiar():
    entry_lado.delete(0, tk.END)
    resultado_area.delete(0, tk.END)
    resultado_perimetro.delete(0, tk.END)
    resultado_altura.delete(0, tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Triángulo equilátero")

# Widgets de la GUI
label_lado = tk.Label(ventana, text="Ingrese el lado del triángulo equilátero: ")
label_lado.grid(row=0, column=0, padx=10, pady=5)

entry_lado = tk.Entry(ventana)
entry_lado.grid(row=0, column=1, padx=10, pady=5)

boton_calcular_area = tk.Button(ventana, text="Calcular el área", command=GUI)
boton_calcular_area.grid(row=1, column=0, columnspan=1, pady=10)

resultado_area = tk.Entry(ventana)
resultado_area.grid(row=1, column=1, padx=10, pady=5)

boton_calcular_perimetro = tk.Button(ventana, text="Calcular el perímetro", command=GUI)
boton_calcular_perimetro.grid(row=2, column=0, columnspan=1, pady=10)

resultado_perimetro = tk.Entry(ventana)
resultado_perimetro.grid(row=2, column=1, padx=10, pady=5)

boton_calcular_altura = tk.Button(ventana, text="Calcular la altura", command=GUI)
boton_calcular_altura.grid(row=3, column=0, columnspan=1, pady=10)

resultado_altura = tk.Entry(ventana)
resultado_altura.grid(row=3, column=1, padx=10, pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=4, column=0, columnspan=4, pady=10)

# Bucle principal
ventana.mainloop()


