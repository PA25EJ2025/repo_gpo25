class Numeros:

    def __init__(self,numero1,numero2,numero3):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3

    def sumar(self):
        return self.numero1 + self.numero2 + self.numero3
    
    def mayor(self):
        return max(self.numero1,self.numero2,self.numero3)
    
    def menor(self):
        return min(self.numero1,self.numero2,self.numero3)
    
    def Iguales(self):
        if self.numero1 == self.numero2 and self.numero2 == self.numero3:
            return True
        else:
            return False
        
    def Concatenar(self):
        return str(self.num1) + str(self.num2) + str(self.num3)
    
    