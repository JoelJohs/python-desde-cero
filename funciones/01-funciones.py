nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

def hola(nombre="John", apellido="Doe"): # Definición de la función hola con un parámetro nombre y un parámetro apellido con valores por defecto "John" y "Doe" respectivamente
    print(f"Hola {nombre} {apellido}")
    print("Al curso Ultimate Python")

hola(nombre, apellido) # Llamado de la función hola con el parámetro nombre y el parámetro apellido
print("") # Salto de línea
hola("Juan", "Perez") # Llamado de la función hola con el parámetro "Juan" y el parámetro "Perez"
print("")
hola() # Llamado de la función hola sin parámetros
print("")
hola(apellido="Campusano", nombre="Dariana") # Llamado de la función hola con el parámetro apellido y el parámetro nombre en diferente orden de los parámetros de la función hola 