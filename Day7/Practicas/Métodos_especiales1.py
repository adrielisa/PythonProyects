""" 
Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima 
el objeto, devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas dobles)
"""

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    #Sirve por si se crea un objeto de clase libro y se busca hacer un print del
    #Objeto, este devolverá lo del return
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}' 