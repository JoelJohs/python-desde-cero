# and, or, not

gas = True
encendido = True
edad = 25

if gas and encendido: # Si gas y encendido son True entonces se ejecuta el bloque de codigo
    print("puedes avanzar")

if gas or encendido: # Si gas o encendido son True entonces se ejecuta el bloque de codigo
    print("puedes avanzar")

if not gas and (encendido or edad > 18): # Si gas es False y encendido o edad > 18 son True entonces se ejecuta el bloque de codigo
    print("puedes avanzar")
# Siempre ejecuta primero los parentesis y luego el not


