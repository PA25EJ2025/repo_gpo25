class MiClase:
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
    def Sumar(self):
       return sum([self.num1+self.num2+self.num3])
    def Mayor(self):
       return max(self.num1,self.num2,self.num3)
    def Menor(self):
       return min(self.num1,self.num2,self.num3)
    def Iguales(self):
      if self.num1 == self.num2 and self.num1==self.num3:
         return True
    def Concatenar(self):
      return str(self.num1)+ str(self.num2) +str(self.num3)
numero1=int(input("Ingresa un numero"))
numero2=int(input("Ingresa un numero"))
numero3=int(input("Ingresa un numero"))
numeritos=MiClase(numero1,numero2,numero3)
print(f"Suma:",numeritos.Sumar())
print(f"Mayor:",numeritos.Mayor())
print(f"Menor",numeritos.Menor())
print(f"Iguales",numeritos.Iguales())
print(f"Concatenar:",numeritos.Concatenar())