""" 
Abre el archivo texto.txt e imprime únicamente la segunda línea.
"""

abrir = open('texto.txt')
leer = abrir.readline()
leer2 = abrir.readline()

print(leer2)

abrir.close()