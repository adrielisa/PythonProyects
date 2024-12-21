"""
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) 
siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma
"""

lista_numeros = [-10,1111,10,20,70]

def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n > 0 and n < 1000:
            suma = suma + n
    return suma
        
suma = suma_menores(lista_numeros)
print(suma)