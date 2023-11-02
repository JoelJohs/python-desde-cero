def get_product(**datos):  # **kwargs -> Diccionario de argumentos con nombre (clave-valor)
    print(datos["id"], datos["name"], datos["price"])


get_product(id="53",
            name="Celular chido",
            price="$12,459")
