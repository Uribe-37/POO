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
        return "El estudiante con número de inscripcion {} y nombres {} debe pagar $ {}".format(self.Ni,self.Nombres,Pago_matricula)
    
Ni = str(input("Ingrese el número de inscripción del estudiante: "))
Nombres = input("Ingrese los nombres del estudiante: ")
Patrimonio = float(input("Ingrese el patrimonio del estudiante: "))
Estrato = int(input("Ingrese el estrato del estudiante: "))
Estudiante = PagoMatricula(Ni,Nombres,Patrimonio,Estrato).Matricula()
print(Estudiante)