#Existen 3 maneras de "abrir" un archivo: solo lectura (r), escribir (w), escribir después de todo lo que contenga el archivo (a)

archivo = open('Day6/Ejercicios/prueba1.txt', 'w')
archivo.write('soy el nuevo texto impostor')
archivo.writelines(['hola', 'mundo', 'aqui', 'estoy'])
archivo.close()

