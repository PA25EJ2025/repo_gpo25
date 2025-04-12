class Numeros:
    def __init__ (self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def SUMA(self):
        return(self.num1) + (self.num2) + (self.num3)
    
    def MAYOR(self):
        return max(self.num1, self.num2, self.num3)
    
    def MENOR(self):
        return min(self.num1, self.num2, self.num3)
    
    def CONCATENAR(self):
        Conca = (str(self.num1)) + (str(self.num2)) + (str(self.num3))
        return Conca
