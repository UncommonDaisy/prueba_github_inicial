def contar_letras(palabra):
    palabra_sin_espacios = palabra.replace(' ', '')
    n=len(palabra_sin_espacios)
    return n

contar_letras('hola')
print(contar_letras('hola'))
