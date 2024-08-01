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
            print(self.nombre, ":", salario_mensual)
        else:
            print(self.nombre)

def main():
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    salario_por_hora = float(input("Ingrese el salario por hora del empleado: "))
    horas_trabajadas = float(input("Ingrese el número de horas trabajadas en el mes: "))

    empleado = Empleado(nombre_empleado, salario_por_hora, horas_trabajadas)
    empleado.comentario_salario()
    
if __name__ == "__main__":
    main()
