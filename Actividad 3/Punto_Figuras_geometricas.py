import math

class Circulo:
  def __init__(self, radio):
    self.radio = radio

  def calcular_area(self):
      return math.pi * math.pow(self.radio,2)
    
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

class Triangulo_rectangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def calcular_area(self):
    return (self.base * self.altura) / 2

  def calcular_perimetro(self):
    return self.base + self.altura + self.calcular_hipotenusa()
  
  def calcular_hipotenusa(self):
    return math.sqrt(math.pow(self.base,2) + math.pow(self.altura,2))
  
  def clasificar_triangulo(self):
    if ((self.base == self.altura) and (self.base == self.calcular_hipotenusa()) and (self.altura == self.calcular_hipotenusa())):
      return "Es un triángulo equilátero"
    elif ((self.base != self.altura) and (self.base != self.calcular_hipotenusa()) and (self.altura != self.calcular_hipotenusa())):
      return "Es un triángulo escaleno"
    else:
      return "Es un triángulo isósceles"
  

class Figuras:
  @staticmethod
  def main():
    figura1 = Circulo(2)
    figura2 = Rectangulo(1, 2)
    figura3 = Cuadrado(3)
    figura4 = Triangulo_rectangulo(3, 5)

    print("El área del círculo es =", figura1.calcular_area())
    print("El perímetro del círculo es =", figura1.calcular_perimetro())

    print("\nEl área del rectángulo es =", figura2.calcular_area())
    print("El perímetro del rectángulo es =", figura2.calcular_perimetro())

    print("\nEl área del cuadrado es =", figura3.calcular_area())
    print("El perímetro del cuadrado es =", figura3.calcular_perimetro())

    print("\nEl área del triángulo es =", figura4.calcular_area())
    print("El perímetro del triángulo es =", figura4.calcular_perimetro())
    print(figura4.clasificar_triangulo())

if __name__ == '__main__':
  Figuras.main()