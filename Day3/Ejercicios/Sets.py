mi_set = set({1,2,3,4,5})
print(type(mi_set))
print(mi_set)

print(2 in mi_set)


s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2) #Unir 2 sets
s3.discard(2) #Eliminar del set lo que ingrese en el parámetro
sorteo = s3.pop() #Elimina al azar una cosa del set
s3.clear() #Vacía al set
print(s3)