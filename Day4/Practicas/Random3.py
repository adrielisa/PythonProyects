"""
Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
"""
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

from random import choice

sorteo = choice(nombres)
print(sorteo)