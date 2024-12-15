mi_lista = ['a', 'b', 'c']
otra_lista = ['hola', 55.3]
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2

print(type(mi_lista))
print(mi_lista3)


mi_lista3[0] = 'alfa' #Podemos modificar un objeto dentro de la lista
mi_lista3.append('g')
mi_lista3.pop() #Dentro del paréntesis puedo seleccionar que índice elimino
print(mi_lista3)


lista = ['y', 'z', 'ff', '132', 'b', 'a12d']
nueva_lista = lista.sort() #Orderna la lista, podemos ordenarlo en reversa con .reverse
print(lista)