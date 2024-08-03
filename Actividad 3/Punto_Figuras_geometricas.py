import tkinter as tk
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * self.base + 2 * self.altura

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self):
        return math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))

    def clasificar_triangulo(self):
        if self.base == self.altura == self.calcular_hipotenusa():
            return "Es un triángulo equilátero"
        elif self.base != self.altura != self.calcular_hipotenusa():
            return "Es un triángulo escaleno"
        else:
            return "Es un triángulo isósceles"

def calcular_area_circulo():
    try:
        radio = float(entry_radio.get())
        figura = Circulo(radio)
        resultado_area_circulo.config(state=tk.NORMAL)
        resultado_area_circulo.delete("1.0", tk.END)
        resultado_area_circulo.insert(tk.END, f"Área: {figura.calcular_area():.2f}")
        resultado_area_circulo.config(state=tk.DISABLED)
    except ValueError:
        resultado_area_circulo.config(state=tk.NORMAL)
        resultado_area_circulo.delete("1.0", tk.END)
        resultado_area_circulo.insert(tk.END, "Error: ingresa un radio válido")
        resultado_area_circulo.config(state=tk.DISABLED)

def calcular_perimetro_circulo():
    try:
        radio = float(entry_radio.get())
        figura = Circulo(radio)
        resultado_perimetro_circulo.config(state=tk.NORMAL)
        resultado_perimetro_circulo.delete("1.0", tk.END)
        resultado_perimetro_circulo.insert(tk.END, f"Perímetro: {figura.calcular_perimetro():.2f}")
        resultado_perimetro_circulo.config(state=tk.DISABLED)
    except ValueError:
        resultado_perimetro_circulo.config(state=tk.NORMAL)
        resultado_perimetro_circulo.delete("1.0", tk.END)
        resultado_perimetro_circulo.insert(tk.END, "Error: ingresa un radio válido")
        resultado_perimetro_circulo.config(state=tk.DISABLED)

def limpiar_circulo():
    entry_radio.delete(0, tk.END)
    resultado_area_circulo.config(state=tk.NORMAL)
    resultado_area_circulo.delete("1.0", tk.END)
    resultado_area_circulo.config(state=tk.DISABLED)
    resultado_perimetro_circulo.config(state=tk.NORMAL)
    resultado_perimetro_circulo.delete("1.0", tk.END)
    resultado_perimetro_circulo.config(state=tk.DISABLED)

def calcular_area_cuadrado():
    try:
        lado = float(entry_lado_cuadrado.get())
        figura = Cuadrado(lado)
        resultado_area_cuadrado.config(state=tk.NORMAL)
        resultado_area_cuadrado.delete("1.0", tk.END)
        resultado_area_cuadrado.insert(tk.END, f"Área: {figura.calcular_area():.2f}")
        resultado_area_cuadrado.config(state=tk.DISABLED)
    except ValueError:
        resultado_area_cuadrado.config(state=tk.NORMAL)
        resultado_area_cuadrado.delete("1.0", tk.END)
        resultado_area_cuadrado.insert(tk.END, "Error: ingresa un lado válido")
        resultado_area_cuadrado.config(state=tk.DISABLED)

def calcular_perimetro_cuadrado():
    try:
        lado = float(entry_lado_cuadrado.get())
        figura = Cuadrado(lado)
        resultado_perimetro_cuadrado.config(state=tk.NORMAL)
        resultado_perimetro_cuadrado.delete("1.0", tk.END)
        resultado_perimetro_cuadrado.insert(tk.END, f"Perímetro: {figura.calcular_perimetro():.2f}")
        resultado_perimetro_cuadrado.config(state=tk.DISABLED)
    except ValueError:
        resultado_perimetro_cuadrado.config(state=tk.NORMAL)
        resultado_perimetro_cuadrado.delete("1.0", tk.END)
        resultado_perimetro_cuadrado.insert(tk.END, "Error: ingresa un lado válido")
        resultado_perimetro_cuadrado.config(state=tk.DISABLED)

def limpiar_cuadrado():
    entry_lado_cuadrado.delete(0, tk.END)
    resultado_area_cuadrado.config(state=tk.NORMAL)
    resultado_area_cuadrado.delete("1.0", tk.END)
    resultado_area_cuadrado.config(state=tk.DISABLED)
    resultado_perimetro_cuadrado.config(state=tk.NORMAL)
    resultado_perimetro_cuadrado.delete("1.0", tk.END)
    resultado_perimetro_cuadrado.config(state=tk.DISABLED)

def calcular_area_rectangulo():
    try:
        base = float(entry_base_rectangulo.get())
        altura = float(entry_altura_rectangulo.get())
        figura = Rectangulo(base, altura)
        resultado_area_rectangulo.config(state=tk.NORMAL)
        resultado_area_rectangulo.delete("1.0", tk.END)
        resultado_area_rectangulo.insert(tk.END, f"Área: {figura.calcular_area():.2f}")
        resultado_area_rectangulo.config(state=tk.DISABLED)
    except ValueError:
        resultado_area_rectangulo.config(state=tk.NORMAL)
        resultado_area_rectangulo.delete("1.0", tk.END)
        resultado_area_rectangulo.insert(tk.END, "Error: ingresa números válidos")
        resultado_area_rectangulo.config(state=tk.DISABLED)

def calcular_perimetro_rectangulo():
    try:
        base = float(entry_base_rectangulo.get())
        altura = float(entry_altura_rectangulo.get())
        figura = Rectangulo(base, altura)
        resultado_perimetro_rectangulo.config(state=tk.NORMAL)
        resultado_perimetro_rectangulo.delete("1.0", tk.END)
        resultado_perimetro_rectangulo.insert(tk.END, f"Perímetro: {figura.calcular_perimetro():.2f}")
        resultado_perimetro_rectangulo.config(state=tk.DISABLED)
    except ValueError:
        resultado_perimetro_rectangulo.config(state=tk.NORMAL)
        resultado_perimetro_rectangulo.delete("1.0", tk.END)
        resultado_perimetro_rectangulo.insert(tk.END, "Error: ingresa números válidos")
        resultado_perimetro_rectangulo.config(state=tk.DISABLED)

def limpiar_rectangulo():
    entry_base_rectangulo.delete(0, tk.END)
    entry_altura_rectangulo.delete(0, tk.END)
    resultado_area_rectangulo.config(state=tk.NORMAL)
    resultado_area_rectangulo.delete("1.0", tk.END)
    resultado_area_rectangulo.config(state=tk.DISABLED)
    resultado_perimetro_rectangulo.config(state=tk.NORMAL)
    resultado_perimetro_rectangulo.delete("1.0", tk.END)
    resultado_perimetro_rectangulo.config(state=tk.DISABLED)

def calcular_area_triangulo():
    try:
        base = float(entry_base_triangulo.get())
        altura = float(entry_altura_triangulo.get())
        figura = TrianguloRectangulo(base, altura)
        resultado_area_triangulo.config(state=tk.NORMAL)
        resultado_area_triangulo.delete("1.0", tk.END)
        resultado_area_triangulo.insert(tk.END, f"Área: {figura.calcular_area():.2f}")
        resultado_area_triangulo.config(state=tk.DISABLED)
    except ValueError:
        resultado_area_triangulo.config(state=tk.NORMAL)
        resultado_area_triangulo.delete("1.0", tk.END)
        resultado_area_triangulo.insert(tk.END, "Error: ingresa números válidos")
        resultado_area_triangulo.config(state=tk.DISABLED)

def calcular_perimetro_triangulo():
    try:
        base = float(entry_base_triangulo.get())
        altura = float(entry_altura_triangulo.get())
        figura = TrianguloRectangulo(base, altura)
        resultado_perimetro_triangulo.config(state=tk.NORMAL)
        resultado_perimetro_triangulo.delete("1.0", tk.END)
        resultado_perimetro_triangulo.insert(tk.END, f"Perímetro: {figura.calcular_perimetro():.2f}")
        resultado_perimetro_triangulo.config(state=tk.DISABLED)
    except ValueError:
        resultado_perimetro_triangulo.config(state=tk.NORMAL)
        resultado_perimetro_triangulo.delete("1.0", tk.END)
        resultado_perimetro_triangulo.insert(tk.END, "Error: ingresa números válidos")
        resultado_perimetro_triangulo.config(state=tk.DISABLED)

def clasificar_triangulo():
    try:
        base = float(entry_base_triangulo.get())
        altura = float(entry_altura_triangulo.get())
        figura = TrianguloRectangulo(base, altura)
        resultado_clasificacion_triangulo.config(state=tk.NORMAL)
        resultado_clasificacion_triangulo.delete("1.0", tk.END)
        resultado_clasificacion_triangulo.insert(tk.END, figura.clasificar_triangulo())
        resultado_clasificacion_triangulo.config(state=tk.DISABLED)
    except ValueError:
        resultado_clasificacion_triangulo.config(state=tk.NORMAL)
        resultado_clasificacion_triangulo.delete("1.0", tk.END)
        resultado_clasificacion_triangulo.insert(tk.END, "Error: ingresa números válidos")
        resultado_clasificacion_triangulo.config(state=tk.DISABLED)

def limpiar_triangulo():
    entry_base_triangulo.delete(0, tk.END)
    entry_altura_triangulo.delete(0, tk.END)
    resultado_area_triangulo.config(state=tk.NORMAL)
    resultado_area_triangulo.delete("1.0", tk.END)
    resultado_area_triangulo.config(state=tk.DISABLED)
    resultado_perimetro_triangulo.config(state=tk.NORMAL)
    resultado_perimetro_triangulo.delete("1.0", tk.END)
    resultado_perimetro_triangulo.config(state=tk.DISABLED)
    resultado_clasificacion_triangulo.config(state=tk.NORMAL)
    resultado_clasificacion_triangulo.delete("1.0", tk.END)
    resultado_clasificacion_triangulo.config(state=tk.DISABLED)

# Ventana principal
ventana = tk.Tk()
ventana.title("Figuras Geométricas")
ventana.geometry("600x600")

# Creación de frames
frame_circulo = tk.LabelFrame(ventana, bd=2, relief=tk.RIDGE, text="Círculo")
frame_circulo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

frame_rectangulo = tk.LabelFrame(ventana, bd=2, relief=tk.RIDGE, text="Rectángulo")
frame_rectangulo.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

frame_cuadrado = tk.LabelFrame(ventana, bd=2, relief=tk.RIDGE, text="Cuadrado")
frame_cuadrado.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

frame_triangulo = tk.LabelFrame(ventana, bd=2, relief=tk.RIDGE, text="Triángulo rectángulo")
frame_triangulo.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)

# Widgets para el círculo
label_radio = tk.Label(frame_circulo, text="Radio del círculo:")
label_radio.grid(row=0, column=0, padx=5, pady=5)

entry_radio = tk.Entry(frame_circulo)
entry_radio.grid(row=0, column=1, padx=5, pady=5)

boton_calcular_area_circulo = tk.Button(frame_circulo, text="Calcular área", command=calcular_area_circulo)
boton_calcular_area_circulo.grid(row=1, column=0, columnspan=2, pady=5)

resultado_area_circulo = tk.Text(frame_circulo, height=1, width=20, state=tk.DISABLED)
resultado_area_circulo.grid(row=2, column=0, columnspan=2, pady=5)

boton_calcular_perimetro_circulo = tk.Button(frame_circulo, text="Calcular perímetro", command=calcular_perimetro_circulo)
boton_calcular_perimetro_circulo.grid(row=3, column=0, columnspan=2, pady=5)

resultado_perimetro_circulo = tk.Text(frame_circulo, height=1, width=20, state=tk.DISABLED)
resultado_perimetro_circulo.grid(row=4, column=0, columnspan=2, pady=5)

boton_limpiar_circulo = tk.Button(frame_circulo, text="Limpiar", command=limpiar_circulo)
boton_limpiar_circulo.grid(row=5, column=0, columnspan=2, pady=5)

# Widgets para el rectángulo
label_base_rectangulo = tk.Label(frame_rectangulo, text="Base del rectángulo:")
label_base_rectangulo.grid(row=0, column=0, padx=5, pady=5)

entry_base_rectangulo = tk.Entry(frame_rectangulo)
entry_base_rectangulo.grid(row=0, column=1, padx=5, pady=5)

label_altura_rectangulo = tk.Label(frame_rectangulo, text="Altura del rectángulo:")
label_altura_rectangulo.grid(row=1, column=0, padx=5, pady=5)

entry_altura_rectangulo = tk.Entry(frame_rectangulo)
entry_altura_rectangulo.grid(row=1, column=1, padx=5, pady=5)

boton_calcular_area_rectangulo = tk.Button(frame_rectangulo, text="Calcular área", command=calcular_area_rectangulo)
boton_calcular_area_rectangulo.grid(row=2, column=0, columnspan=2, pady=5)

resultado_area_rectangulo = tk.Text(frame_rectangulo, height=1, width=20, state=tk.DISABLED)
resultado_area_rectangulo.grid(row=3, column=0, columnspan=2, pady=5)

boton_calcular_perimetro_rectangulo = tk.Button(frame_rectangulo, text="Calcular perímetro", command=calcular_perimetro_rectangulo)
boton_calcular_perimetro_rectangulo.grid(row=4, column=0, columnspan=2, pady=5)

resultado_perimetro_rectangulo = tk.Text(frame_rectangulo, height=1, width=20, state=tk.DISABLED)
resultado_perimetro_rectangulo.grid(row=5, column=0, columnspan=2, pady=5)

boton_limpiar_rectangulo = tk.Button(frame_rectangulo, text="Limpiar", command=limpiar_rectangulo)
boton_limpiar_rectangulo.grid(row=6, column=0, columnspan=2, pady=5)

# Widgets para el cuadrado
label_lado_cuadrado = tk.Label(frame_cuadrado, text="Lado del cuadrado:")
label_lado_cuadrado.grid(row=0, column=0, padx=5, pady=5)

entry_lado_cuadrado = tk.Entry(frame_cuadrado)
entry_lado_cuadrado.grid(row=0, column=1, padx=5, pady=5)

boton_calcular_area_cuadrado = tk.Button(frame_cuadrado, text="Calcular área", command=calcular_area_cuadrado)
boton_calcular_area_cuadrado.grid(row=1, column=0, columnspan=2, pady=5)

resultado_area_cuadrado = tk.Text(frame_cuadrado, height=1, width=20, state=tk.DISABLED)
resultado_area_cuadrado.grid(row=2, column=0, columnspan=2, pady=5)

boton_calcular_perimetro_cuadrado = tk.Button(frame_cuadrado, text="Calcular perímetro", command=calcular_perimetro_cuadrado)
boton_calcular_perimetro_cuadrado.grid(row=3, column=0, columnspan=2, pady=5)

resultado_perimetro_cuadrado = tk.Text(frame_cuadrado, height=1, width=20, state=tk.DISABLED)
resultado_perimetro_cuadrado.grid(row=4, column=0, columnspan=2, pady=5)

boton_limpiar_cuadrado = tk.Button(frame_cuadrado, text="Limpiar", command=limpiar_cuadrado)
boton_limpiar_cuadrado.grid(row=5, column=0, columnspan=2, pady=5)

# Widgets para el triángulo
label_base_triangulo = tk.Label(frame_triangulo, text="Base del triángulo:")
label_base_triangulo.grid(row=0, column=0, padx=5, pady=5)

entry_base_triangulo = tk.Entry(frame_triangulo)
entry_base_triangulo.grid(row=0, column=1, padx=5, pady=5)

label_altura_triangulo = tk.Label(frame_triangulo, text="Altura del triángulo:")
label_altura_triangulo.grid(row=1, column=0, padx=5, pady=5)

entry_altura_triangulo = tk.Entry(frame_triangulo)
entry_altura_triangulo.grid(row=1, column=1, padx=5, pady=5)

boton_calcular_area_triangulo = tk.Button(frame_triangulo, text="Calcular área", command=calcular_area_triangulo)
boton_calcular_area_triangulo.grid(row=2, column=0, columnspan=2, pady=5)

resultado_area_triangulo = tk.Text(frame_triangulo, height=1, width=20, state=tk.DISABLED)
resultado_area_triangulo.grid(row=3, column=0, columnspan=2, pady=5)

boton_calcular_perimetro_triangulo = tk.Button(frame_triangulo, text="Calcular perímetro", command=calcular_perimetro_triangulo)
boton_calcular_perimetro_triangulo.grid(row=4, column=0, columnspan=2, pady=5)

resultado_perimetro_triangulo = tk.Text(frame_triangulo, height=1, width=20, state=tk.DISABLED)
resultado_perimetro_triangulo.grid(row=5, column=0, columnspan=2, pady=5)

boton_clasificar_triangulo = tk.Button(frame_triangulo, text="Clasificar triángulo", command=clasificar_triangulo)
boton_clasificar_triangulo.grid(row=6, column=0, columnspan=2, pady=5)

resultado_clasificacion_triangulo = tk.Text(frame_triangulo, height=1, width=25, state=tk.DISABLED)
resultado_clasificacion_triangulo.grid(row=7, column=0, columnspan=2, pady=5)

boton_limpiar_triangulo = tk.Button(frame_triangulo, text="Limpiar", command=limpiar_triangulo)
boton_limpiar_triangulo.grid(row=8, column=0, columnspan=2, pady=5)

# Bucle principal
ventana.mainloop()
