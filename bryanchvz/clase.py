class Mi_clase:
    def __init__(self,num1:int,num2:int,num3:int):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        
    def sumar(self):
        resultado = self.num1 + self.num2 + self.num3
        return resultado
    
    def mayor(self):
        resultado = max(self.num1,self.num2,self.num3)
        return resultado
    
    def menor(self):
        resultado = min(self.num1,self.num2,self.num3)
        return resultado
    
    def iguales(self):
        if self.num1 == self.num2 and self.num2 == self.num3:
            resultado = True
        else:
            resultado = False
        return resultado
    
    def concatenar(self):
        concatenado = str(self.num1) + str(self.num2) + str(self.num3)
        return concatenado

num1 = int(input("Ingresa un primer numero: "))
num2 = int(input("Ingresa un segundo numero: "))
num3 = int(input("Ingresa un tercer numero: "))
num_nuevo = Mi_clase(num1,num2,num3)

print("La suma es: ", num_nuevo.sumar())
print("El numero mayor es: ",num_nuevo.mayor())
print("Los numeros son iguales? true/false: ", num_nuevo.iguales())
print("Numeros concatenados: ", num_nuevo.concatenar())