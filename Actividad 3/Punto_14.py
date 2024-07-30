class Incentivos():
    def __init__(self, Vd1,Vd2,Vd3,Salar):
        self.Vd1 = Vd1
        self.Vd2 = Vd2
        self.Vd3 = Vd3
        self.Salar = Salar
    
    def Salarios(self):
        TVentas = self.Vd1 + self.Vd2 + self.Vd3
        PorVen = 0.33*TVentas
        if self.Vd1 > PorVen:
            Salar1=self.Salar+0.2*self.Salar
        if self.Vd1 < PorVen:
            Salar1=self.Salar
        if self.Vd2 > PorVen:
            Salar2=self.Salar+0.2*self.Salar
        if self.Vd2 < PorVen:
            Salar2=self.Salar
        if self.Vd3 > PorVen:
            Salar3=self.Salar+0.2*self.Salar
        if self.Vd3 < PorVen:
            Salar3=self.Salar
        return "Salario vendedores depto 1: $ {}, Salario vendedores depto 2: $ {} y Salario vendedores depto 3: $ {}".format(Salar1,Salar2,Salar3)
    def __str__(self):
        return "{}".format(self.Salarios())
    
Vd1 = float(input("Ingrese el valor de las ventas del departamento 1: "))
Vd2 = float(input("Ingrese el valor de las ventas del departamento 2: "))
Vd3 = float(input("Ingrese el valor de las ventas del departamento 3: "))
Salar = float(input("Ingrese el salario base: "))
Vendedores = Incentivos(Vd1,Vd2,Vd3,Salar)
print(Vendedores)
