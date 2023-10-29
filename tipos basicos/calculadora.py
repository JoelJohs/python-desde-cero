n1 = input("Ingresa un numero: ")  # input() siempre devuelve un string
n2 = input("Ingresa otro numero: ")  # input() siempre devuelve un string

n1 = int(n1)  # Convertimos el string a entero
n2 = int(n2)  # Convertimos el string a entero

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2}: la suma es {suma}
la resta es {resta}
la multiplicacion es {multiplicacion}
la division es {division}
"""  # f es para indicar que es un string con formato o concatenacion de variables

print(mensaje)
