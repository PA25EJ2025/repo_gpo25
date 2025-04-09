class Mi_clase:
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def sumar(self):
        resultado = self.num1 + self.num2 + self.num3
        return resultado

    def mayor(self):
        resultado = max(self.num1, self.num2, self.num3)
        return resultado
    
    def menor(self):
        resultado = min(self.num1, self.num2, self.num3)
        return resultado

    def iguales(self):
        if self.num1 == self.num2 and self.num2 == self.num3:
            resultado = True
        else:
            resultado = False
        return resultado 

    def concatenar(self):
        num_concat = "{}{}{}".format(self.num1,self.num2,self.num3)
        return num_concat
    

nuevo_numero = Mi_clase(1,2,3)

print(nuevo_numero.sumar())
print(nuevo_numero.mayor())
print(nuevo_numero.menor())
print(nuevo_numero.iguales())
print(nuevo_numero.concatenar())

