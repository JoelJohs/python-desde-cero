animal = "  nutria DE Rio  "  # String

print(animal.upper())  # Convierte a mayusculas
print(animal.lower())  # Convierte a minusculas
print(animal.capitalize())
# Convierte a mayuscula la primera letra de cada palabra, en caso de que el inicio sea espacio en blanco, deja todo en minuscula

print(animal.title())  # Convierte a mayuscula la primera letra de cada palabra
print(animal.strip())  # Elimina los espacios en blanco al inicio y al final

# concatenacion de metodos


print(animal.strip().capitalize())
# Elimina los espacios en blanco al inicio y al final y convierte a mayuscula la primera letra de cada palabra

print(animal.find("DE"))  # Busca la posicion de la primera coincidencia

print(animal.replace("DE", "Chida de"))  # Reemplaza la primera coincidencia

print("DE" in animal)  # Busca la primera coincidencia y devuelve True o False

print("DE" not in animal)
# Busca la primera coincidencia y devuelve True o False
