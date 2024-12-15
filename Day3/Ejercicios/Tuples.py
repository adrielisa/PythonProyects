mi_tuple = (1,2,(10,20),4) #Pueden construirse sin parentesis y con cualquier tipo de objeto

print(mi_tuple[0]) #Para buscar un elemento
print(mi_tuple[2][0])

#Para añadir elementos de un tupple a variables
t = 10,9,11
x, y, z = t
print(x,y,z)

#Para contar cuantos elementos repetidos hay, puedo modificar el count por index y me muestra en donde
#se encuentra lo que tengo en el paréntesis

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

print(mi_tupla.count(2))