""" 
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
"""
# Abrir el archivo en modo escritura (w) y cambiar su contenido
archivo = open('mi_archivo.txt', 'w')
archivo.write('Nuevo texto')  # Escribir el nuevo texto en el archivo
archivo.close()  # Cerrar el archivo después de escribir

# Abrir el archivo en modo lectura (r) para leer su contenido
archivo = open('mi_archivo.txt', 'r')
contenido = archivo.read()  # Leer todo el contenido del archivo
archivo.close()  # Cerrar el archivo después de leer

# Imprimir el contenido del archivo
print(contenido)