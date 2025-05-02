class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def sumar(self) -> int:
        return self.num1 + self.num2 + self.num3

    def mayor(self) -> int:
        return max(self.num1, self.num2, self.num3)

    def menor(self) -> int:
        return min(self.num1, self.num2, self.num3)

    def iguales(self) -> bool:
        return self.num1 == self.num2 == self.num3

    def concatenar(self) -> str:
        return f"{self.num1}{self.num2}{self.num3}"


nuevo_numero = Mi_Clase(1, 2, 3)

print(nuevo_numero.sumar())        
print(nuevo_numero.mayor())        
print(nuevo_numero.menor())        
print(nuevo_numero.iguales())     
print(nuevo_numero.concatenar())   
