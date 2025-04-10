class Mi_clase:
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def suma(self):
        return sum(self.num1,self.num2,self.num3)
    
    def mayor(self):
        if self.num1 > self.num2 and self.num1 > self.num3:
            print(self.num1)
        elif self.num2 > self.num1 and self.num2 > self.num3:
            print(self.num2)
        elif self.num3 > self.num1 and self.num3 > self.num2:
            print(self.num3)

    def menor(self):
        if self.num1 < self.num2 and self.num1 < self.num3:
            print(self.num1)
        elif self.num2 < self.num1 and self.num2 < self.num3:
            print(self.num2)
        elif self.num3 < self.num1 and self.num3 < self.num2:
            print(self.num3)

    def iguales(self):
        return self.num1 == self.num2 == self.num3

    def concatenar(self):
        return f"{self.num1}{self.num2}{self.num3}"