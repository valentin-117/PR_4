def crear_diccionario(input_str):
    # Crear un diccionario vacío
    diccionario = {}
    # Separar las entradas por comas
    entradas = input_str.split(',')
    for entrada in entradas:
        # Separar la palabra y su traducción por dos puntos
        par = entrada.split(':')
        if len(par) == 2:
            palabra_espanol = par[0].strip()
            traduccion_ingles = par[1].strip()
            diccionario[palabra_espanol] = traduccion_ingles
    return diccionario

def traducir_frase(diccionario, frase):
    # Separar la frase en palabras
    palabras = frase.split()
    traduccion = []
    for palabra in palabras:
        # Traducir cada palabra si está en el diccionario
        traduccion.append(diccionario.get(palabra, palabra))
    return ' '.join(traduccion)

# Entrada del usuario
input_str = input("Introduce las palabras en español e inglés (formato: español:inglés, ...): ")
diccionario = crear_diccionario(input_str)

frase = input("Introduce una frase en español para traducir: ")
traduccion = traducir_frase(diccionario, frase)

print("Traducción:", traduccion)

