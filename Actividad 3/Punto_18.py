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

Cod= input("Ingrese el código del empleado: ")
Nom= input("Ingrese el nombre del empleado: ")
Horas= float(input("Ingrese el número de horas trabajadas: "))
Valor= float(input("Ingrese el valor de la hora: "))
Ret= float(input("Ingrese el porcentaje de retención: "))
Empleado1 = Empleado(Cod, Nom, Horas, Valor, Ret)
print(Empleado1)

