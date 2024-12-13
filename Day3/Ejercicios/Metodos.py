texto = "Este es el texto de Isai"

resultado = texto.upper() #Pasa todo el texto a mayúscula
resultado2 = texto[2].upper() #Pasa el índice indicado del texto a mayúsculas
resultado3 = texto.lower() #Pasa todo a minúsuclas
resultado4 = texto.split() #Divide el texto por palabras y las almacena en una lista
resultado5 = texto.split("t") #La t es el criterio de separación, se separara cada que haya una t 
resultado6 = texto.find("texto") #Igual a index, solo cambia el mensaje de error
resultado7 = texto.replace("Isai", "todos") #Reemplaza los elementos "Isai" por "todos"

print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)




a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d]) #Une todos los elementos de una lista, con el criterio de dejar un espacio en blanco por cada variable (palabra) de la lista
print(e)

