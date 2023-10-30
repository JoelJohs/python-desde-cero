# numero = 1

# while numero < 100:
#     print(numero)
#     numero *= 2 # Multiplica el valor de numero por 2 de manera continua hasta que numero sea mayor o igual a 100

comando = "" # Inicialmente es un string vacío

# El bucle se ejecuta hasta que el usuario escribe "salir"
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break # Rompe el bucle
