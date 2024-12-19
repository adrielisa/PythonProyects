from random import *

#Para importar un número aleatorio
aleatorio = randint(1,50)
print(aleatorio)

#Para importar un número aleatorio con decimales
aleatorio2 = round(uniform(1,3),2)
print(aleatorio2)

#Para importar un número aleatorio entre 0 y 1
aleatorio3 = random()
print(aleatorio3)

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio4 = choice(colores)
print(aleatorio4)

numeros = list(range(5,50,5))

shuffle(numeros)

print(numeros)