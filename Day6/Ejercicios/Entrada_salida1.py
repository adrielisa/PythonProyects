mi_archivo = open('Day6/Ejercicios/prueba.txt')

#Lee todo el archivo 
print(mi_archivo.read())

#Lee una línea
una_linea = mi_archivo.readline()
print(una_linea)

#Lee una línea
una_linea = mi_archivo.readline()
print(una_linea)


#Lee una línea y elimina el salto de línea
una_linea = mi_archivo.readline()
print(una_linea.rstrip())

#Lee línea x línea y añade texto a cada print de línea
for l in mi_archivo:
    print("Aquí dice: " + l)

#Ahora la líneas son una lista
todas = mi_archivo.readlines()
todas = todas.pop


mi_archivo.close()