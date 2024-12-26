"""Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos
"""

def contar_primos(a):
    lista = list(range(1,a+1))
    lista_primos = []
    for n in lista:
        if n%2 == 0:
            lista_primos.append(n)
    print(f'La cantidad de primos que tienes es {len(lista_primos)}')
    return(print(lista_primos)) 

contar_primos(100)
    
