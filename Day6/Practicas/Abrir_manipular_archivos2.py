""" Imprime la primera línea del archivo texto.txt

No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
Abrir_manipular_archivos1.py
"""

abrir = open('texto.txt')
leer = abrir.readline()
print(leer)

abrir.close()