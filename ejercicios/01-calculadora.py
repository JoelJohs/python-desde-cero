mensaje = """
Digite una de las siguientes opciones:
suma - Para sumar dos números
resta - Para restar dos números
mult - Para multiplicar dos números
div - Para dividir dos números
salir - Para salir del programa
(Ingrese en formato texto):

"""

while True:
    opcion = input(mensaje)
    if opcion.lower() == "suma":
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        print(f"El resultado de la suma es: {n1 + n2}")
    elif opcion.lower() == "resta":
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        print(f"El resultado de la resta es: {n1 - n2}")
    elif opcion.lower() == "mult":
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        print(f"El resultado de la multiplicación es: {n1 * n2}")
    elif opcion.lower() == "div":
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        if n2 == 0:
            print("No se puede dividir por cero")
        else:
            print(f"El resultado de la división es: {n1 / n2}")
    elif opcion.lower() == "salir":
        break
    else:
        print("Digite una opción válida")
