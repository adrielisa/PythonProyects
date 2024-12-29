class Pajaro:
    
    #Este es un atributo de clase, todas las instancias de pajaro lo tendrán
    alas = True
    
    #__init__ es el constructor, self es una convención, color es un parámetro, después agregamos un atributo
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    #Esto es un método de instancia (una función)
    def piar(self):
        print('pio, mi color es {}'.format(self.color)) #Para mostrar el color del pájaro
    
    #Esto es un método de instancia (una función), nos pide un parámetro
    def volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')
        
    def  pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')
        
    #Metodo de clase, es un método que se puede ejecutar sin una instancia
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)
        
    @staticmethod
    def mirar():
        print('El pajaro mira')

Pajaro.mirar()