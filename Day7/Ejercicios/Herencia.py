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
    pass

piolin = Pajaro(2,'amarillo')

print(piolin.color)