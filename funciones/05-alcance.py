# Las variables globales se consideran malas practicas
# ya que se pueden modificar desde cualquier parte del codigo
# y esto puede causar problemas

def saludo():
    saludo = "Hola Mundo"
    print(saludo)


def jojsaludo():
    saludo = "Jojo te saluda"
    print(saludo)

# Se pueden definir los alcances de las variables de la siguiente manera:


# print(saludo) la variable saludo no se puede llamar desde fuera de la funcion
# Lo correcto es colocar un print dentro de la funcion para que se pueda llamar

saludo()
jojsaludo()
saludo()

# La variable saludo es distinta para saludo() y jojsaludo()
# ya que se definen dentro de las funciones y se guardan en diferentes espacios de memoria
# por lo que no se mezclan
