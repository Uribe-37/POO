class TrianguloEquilatero(object):
    
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return (self.lado ** 2) * (3 ** 0.5) / 4

    def perimetro(self):
        return self.lado * 3
    
    def altura(self):
        return (self.lado * (3 ** 0.5)) / 2
    
    def __str__(self):
        return "Lado: {} - Area: {} - Perimetro: {} - Altura: {}".format(self.lado, self.area(), self.perimetro(), self.altura())

Lado= float(input("Ingrese el lado del triangulo: "))
Triangulo1 = TrianguloEquilatero(Lado)

print(Triangulo1)