class Mi_clase:
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def suma(self):
        return self.num1 + self.num2 + self.num3
    
    def mayor(self):
        return max(self.num1,self.num2,self.num3)

    def menor(self):
        return min(self.num1,self.num2,self.num3)
    def iguales(self):
        return self.num1 == self.num2 == self.num3

    def concatenar(self):
        return f"{self.num1}{self.num2}{self.num3}"
    

num = Mi_clase(3,3,3)

print("Suma de los numeros", num.suma())
print("El mayor", num.mayor())
print("El menor", num.menor())
print("Son iguales?", num.iguales())
print("Concatenados", num.concatenar())