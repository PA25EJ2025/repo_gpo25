print("Bienvenido a mi programa")

while True:
    nums = 0
    num1 = int(input("Primer Numero"))
    num2 = int(input("Segundo Numero"))
    num3 = int(input("Tercer Numero"))
    Numeros = nums(num1, num2, num3)
    print("MENU")
    print("1. Sumar numeros")
    print("2. Revisar cual es mayor")
    print("3. Revisar cual es menor")
    print("4. Concatenar los tres numeros")
    print("5. Salir")

    opcion = int(input("Selecciona el numero de la opción que desear ejecutar"))

    if opcion == 1:
        suma = Numeros.SUMA(Numeros)
    elif opcion == 2:
        print(f"El numero mayor es {nums.MAYOR(Numeros)}")
    elif opcion == 3:
        print(f"El numero menor es: {nums.MENOR(Numeros)}")
    elif opcion == 4:
        print(f"Los numeros concatenados son: {nums.CONCATENAR(Numeros)}")
    elif opcion == 5:
        break
    else:
        print("Opcion No valida")



