"""
Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una 
lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.
"""

lista_numeros = [10,-1,-244,3313,-12]
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False
    return True
        
positivos = todos_positivos(lista_numeros)
print(positivos)

