class Mi_clase:
    def __init__(self,n1:int,n2:int,n3:int):
        self.num1 = n1
        self.num2 = n2
        self.num3 = n3
    
    def sumar(self):
        return self.num1 + self.num2 + self.num3
    
    def mayor(self):
        return max(self.num1,self.num2,self.num3)
    
    def menor(self):
        return min(self.num1,self.num2,self.num3)
    
    def iguales(self):
        if self.num1 and self.num2 and self.num3:
            return True
        else:
            return False
        
    def concatenar(self):
        return f'{self.num1}{self.num2}{self.num3}'
    
instance = Mi_clase(3,5,6)
print(instance.sumar())
print(instance.mayor())
print(instance.menor())
print(instance.iguales())
print(instance.concatenar())