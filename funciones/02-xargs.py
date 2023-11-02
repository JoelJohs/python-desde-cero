def suma(*numeros):  # *numeros es una tupla de argumentos variables (xargs)
    resultado = 0
    for numero in numeros:  # Se recorre la tupla de argumentos variables
        resultado += numero
    # Tener cuidado con la identación de esta línea de código para no se ejecute en el ciclo for
    print(resultado)


suma(2, 6)

# Se pueden pasar tantos argumentos como se desee
suma(2, 6, 8, 10, 12, 14, 16, 18, 20)
suma(5, 8, 9, 12)
