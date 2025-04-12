class Mi_clase():
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def sumar(self):
        return sum([self.num1+self.num2+self.num3])
    
    def mayor(self):
        return max(self.num1,self.num2,self.num3)
    
    def menor(self):
        return min(self.num1,self.num2,self.num3)
    
    def iguales(self):
        if self.num1 == self.num2 and self.num2 == self.num3:
            return True
        else:
            return False
    def concatenar(self):
        return str(self.num1) + str(self.num2) + str(self.num3)
    

num1 = int(input("Ingresa un numero"))
num2 = int(input("Ingresa un numero"))
num3 = int(input("Ingresa un numero"))

numeros = Mi_clase(num1, num2, num3)

print(f"Suma de los numeros: ", numeros.sumar())
print(f"El numero mayor es: ", numeros.mayor())
print(f"El numero menor es. ", numeros.menor())
print(f"Los numeros iguales son ", numeros.iguales())
print(f"Concatenar numeros:", numeros.concatenar())