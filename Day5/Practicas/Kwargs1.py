"""
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y
devuelva esa cantidad como resultado.


"""

def cantidad_atributos(**kwargs):
    cantidad = 0
    for _ in kwargs.items():
        cantidad = cantidad + 1 
    return cantidad
    
print(cantidad_atributos(a=1,b=2,c=3))