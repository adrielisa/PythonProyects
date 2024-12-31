#Polimorifismo

""" 
2 objetos de formas distintas pueden ejecutar un método con el mismo nombre
"""

class Vaca:
    
    #Método
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(self.nombre + "dice muuu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(self.nombre + "dice beeee")
        
vaca1 = Vaca('Brissa')
oveja1 = Oveja('Nube')


""" 
Gracias al polimorfismo puedo invocar a 2 clases distintas con el
método hablar() distinto y almacenar esas invocaciones en una lista,
la cual uso para hacer un recorrido con el ciclo for, dependiendo
de que tipo de clase sea el animal de la lista animales es como va a 
"hablar"
"""
animales = [vaca1, oveja1]

for animal in animales:
    animal.hablar()
    
def animal_habla(animal):
    animal.hablar()
    
animal_habla(oveja1)