nombre = "Juan"
apellido = "Perez"

nombre_completo = nombre + " " + apellido  # Concatenacion

print(nombre_completo)

# Otra forma de concatenar

nombre_completo2 = f"{nombre} {apellido}"  # Formato de cadena

print(nombre_completo2)

# Un ejemplo de formato de cadena

ejemplo = f"El nombre completo es {nombre_completo2}, y su longitud es {len(nombre_completo2)}, y su primer caracter es {
    nombre_completo2[0]}, y su ultimo caracter es {nombre_completo2[-1]}"  # Formato de cadena

print(ejemplo)
