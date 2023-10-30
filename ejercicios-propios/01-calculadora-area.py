import math

mensaje = """
Ingrese una opcion
1.- Area de un cuadrado
2.- Area de un triangulo
3.- Area de un circulo
4.- Salir

"""  # Mensaje que se muestra al usuario

aux = input(mensaje)  # Variable auxiliar que almacena la opcion del usuario
print("")
print("")

while True:  # Bucle infinito
    if aux == "1":
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado * lado
        print("El area del cuadrado es: ", area)
        print("")
        aux = input(mensaje)
        print("")
        print("")
    elif aux == "2":
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        area = (base * altura) / 2
        print("El area del triangulo es: ", area)
        print("")
        aux = input(mensaje)
        print("")
        print("")
    elif aux == "3":
        radio = float(input("Ingrese el radio del circulo: "))
        area = 3.1416 * (math.pow(radio, 2))
        print("El area del circulo es: ", area)
        print("")
        aux = input(mensaje)
        print("")
        print("")
    elif aux == "4" or aux.lower() == "salir":
        print("Saliendo del programa...")
        break  # Rompe el bucle
    else:
        print("Opcion invalida")
        print("")
        aux = input(mensaje)
        print("")
        print("")
