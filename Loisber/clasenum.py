class Mi_clase:
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

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

objeto = Mi_clase(num1, num2, num3)

print("\nResultados:")
print("Suma:", objeto.sumar())
print("Mayor:", objeto.mayor())
print("Menor:", objeto.menor())
print("¿Son iguales?:", objeto.iguales())
print("Concatenado:", objeto.concatenar())
