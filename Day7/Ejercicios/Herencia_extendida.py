class Animal:
    
    #Atributos
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    #Método
    def nacer(self):
        print('Este animal ha nacido')

#La clase Pajaro hereda de animal
class Pajaro(Animal):
    
    """Manera 1 de heredar 
    def __init__(self, edad, color, altura):
        self.edad = edad
        self.color = color
        self.altura = altura """
        
    #Manera 2 de heredar
    def __init__(self, edad, color, altura):
        super().__init__(edad, color) #Para heredar todos los atríbutos
        self.altura = altura
        
    def hablar(self):
        print('Pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')

piolin = Pajaro(2,'amarillo', 60)
mi_animal = Animal(5, 'negro')




#Herencia múltiple

class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('ja ja')
    
    def hablar(self):
        print('que tal')

class Hijo(Padre, Madre):
    pass
    
class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.reir()
mi_nieto.hablar()
