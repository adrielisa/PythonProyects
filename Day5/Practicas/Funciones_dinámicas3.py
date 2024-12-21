"""
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
"""

lista_numeros = [10,20,30,42,12,12,35,13,565]

def cantidad_pares(lista_numeros):
    pares = 0
    for n in lista_numeros:
        if n % 2 == 0:
            pares = pares + 1
    return pares

numeros_pares = cantidad_pares(lista_numeros)
print(numeros_pares)