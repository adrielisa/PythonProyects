class Pajaro:
    
    #Este es un atributo de clase, todas las instancias de pajaro lo tendrán
    alas = True
    
    #__init__ es el constructor, self es una convención, color es un parámetro, después agregamos un atributo
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

        
mi_pajaro = Pajaro('negro', 'Tucan')


print(f'Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')

print(Pajaro.alas)
print(mi_pajaro.alas)