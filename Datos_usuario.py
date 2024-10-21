print("")
print("Frías Villa Angel Valentin 3W")
print("")
print("Este es un programa que almacenará los datos ingresados por el usuario")
print("")
# Crea un diccionario vacío
persona = {}

# crea la lista de los datos requeridos
claves = ["Nombre", "Edad", "Sexo", "Teléfono", "Correo electrónico"]

# se crea un bucle pidiendo los datos al ususario
for clave in claves:
    valor = input(f"Introduce {clave}: ")
    persona[clave] = valor
    print("\nContenido del diccionario:")
    for key, value in persona.items():
        print(f"{key}: {value}")
# imprime los datos ingresados por el usuario
print("\nDatos finales de la persona:")
for key, value in persona.items():
    print(f"{key}: {value}")
