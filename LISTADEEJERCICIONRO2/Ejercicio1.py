print("EJERCICIO 1\n")

print("BIENVENIDO A TU MENU ITERATIVO")
while True:
    print("""Escoge una opción que quieras realizar
    1. Realizar un programa que dibuje un cuadrado en consola con *, usando bucles
    2. Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e imprimir el número
    3. Iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad.
    4. Salir
""")
    
    opc = input("Digite una opción: ")
    if opc == '1':
        lado = int(input("Ingrese el lado del cuadrado: "))
        for i in range (1,lado):
            for j in range(1,lado):
                print("*")
    elif opc == '2':
        mi_lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

        for numero in mi_lista:
            if numero%2==0:
               print(numero)
    elif opc == '4':
        print("Gracias por tu visita")
        break
    else:
        break