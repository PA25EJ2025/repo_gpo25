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
    
    def iguales(self):
        if self.numero1 == self.numero2 and self.numero2 == self.numero3:
            return True
        else:
            return False
        
    def concatenar(self):
        return str(self.numero1) + str(self.numero2) + str(self.numero3)
    
numero1=int(input("Ingresa un numero"))
numero2=int(input("Ingresa un numero"))
numero3=int(input("Ingresa un numero"))

conjunto = Numeros(numero1,numero2,numero3)

print(f"Resultado de suma :",conjunto.sumar())
print(f"Resultado de mayor :",conjunto.mayor())
print(f"Resultado de menor :",conjunto.menor())
print(f"Resultado de iguales ",conjunto.iguales())
print(f"Resultado de concatenar :",conjunto.concatenar())