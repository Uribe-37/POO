class NumMayor():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def mayor(self):
        if self.num1 > self.num2:
          return "{} es mayor que {}".format(self.num1, self.num2)
        elif self.num1 == self.num2:
          return "{} es igual a {}".format(self.num1, self.num2)
        else:
            return "{} es mayor que {}".format(self.num1, self.num2)
    
    def __str__(self):
        return "{}".format(self.mayor())

num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))   
NumMayor1 = NumMayor(num1, num2)
print(NumMayor1)