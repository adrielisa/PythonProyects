"""
Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos 
(es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positiv
"""

def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma = suma + abs(arg)
    return(suma)

resultado = suma_absolutos(1,2,3,4,111)
print(resultado)