"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""

def cero_repetido(*args):
    suma_ceros = 0
    for arg in args:
        if arg == 0:
            suma_ceros = suma_ceros + 1
    
    if suma_ceros >= 2:
        return print(True)
    else: return print(False)
    

cero_repetido(1,2,4,6,55,1001,10000)