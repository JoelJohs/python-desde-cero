# for i in range(5): # Itera 5 veces
#     print(i, i * "Hola ") # Imprime el valor de i y multiplica el string "Hola " por el valor de i



buscar = 3

# buscar = int(buscar)

for i in range(10):
    print(i)
    if i == buscar:
        print("Numero", i, "encontrado")
        break # Rompe el bucle
else: #Else va a nivel de for, no de if, ya que si se pone a nivel del if se ejecutara en cada iteracion
    print("Numero 12no encontrado") # En caso de que no se encuentre el numero se ejecuta este bloque de codigo


# Existen muchos iteradores en python, como por ejemplo: listas, tuplas, diccionarios, etc.
# Los strings tambien son iterables, por lo que se puede iterar sobre ellos
# Ejemplo:

for char in "Joel Josafat":
    print(char) # Imprime cada caracter del string