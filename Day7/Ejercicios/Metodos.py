class Pajaro:
    
    #Este es un atributo de clase, todas las instancias de pajaro lo tendrán
    alas = True
    
    #__init__ es el constructor, self es una convención, color es un parámetro, después agregamos un atributo
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    #Esto es un método (una función)
    def piar(self):
        print('pio, mi color es {}'.format(self.color)) #Para mostrar el color del pájaro
    
    #Esto es un método (una función), nos pide un parámetro
    def volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')
        
piolin = Pajaro('Amarillo', 'Canario')

piolin.piar()