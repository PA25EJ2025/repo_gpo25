class Mi_clase:
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def sumar(self):
        return self.num1 + self.num2 + self.num3
    def mayor(self):
        return max(self.num1,self.num2,self.num3)
    def menor(self):
        return min(self.num1,self.num2,self.num3)
    def iguales(self):
        if self.num1 == self.num2 and self.num1 == self.num3:
            return True
        else:
            return False
    def concatenar(self):
        return str(self.num1) + str(self.num2) + str(self.num3)
    
n1 = int(input("Ingrese num1: "))
n2 = int(input("Ingrese num2: "))
n3 = int(input("Ingrese num3: "))

numeros = Mi_clase(n1,n2,n3)
print("Suma:")
print(numeros.sumar())
print("Mayor:")
print(numeros.mayor())
print("Menor:")
print(numeros.menor())
print("Iguales:")
print(numeros.iguales())
print("Concatenar:")
print(numeros.concatenar())