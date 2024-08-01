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
            print("X_1 =", raiz1, " X_2 =", raiz2)
        elif discriminante == 0:
            if self.b == 0:
                raiz = 0
            else:
                raiz = -self.b / (2 * self.a)
            print("La única solución es:", raiz)
        else:
            print("No hay solución en los números reales")

def main():
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    C = float(input("Ingrese el coeficiente C: "))

    ecuacion = EcuacionCuadratica(A, B, C)
    ecuacion.calcular_raices()

if __name__ == "__main__":
    main()
