class Miclase:
    def __init__(self num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        
    def sumar(self):
        return self.num1 + self.num2 + self.num3
        
    def mayor(self):
        return max(self.num1, self.num2, self.num3)
    
    def iguales(self):
        return self.num1 == self.num2 == self.num3
    
    def concatenar(self):
        return f"{self.num1}{self.num2}{self.num3}"
    
obj = Miclase(30,40,40)
print("Suma: ", obj.sumar())
print("mayor: ", obj.mayor())
print("iguales: ", obj.iguales())
print("concatenacion: ", obj.concatenar())