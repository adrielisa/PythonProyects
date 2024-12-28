""" 
Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
"""
abrir = open('mi_archivo.txt', 'a')
abrir.write('Nuevo inicio de sesión')
abrir.close

abrir = open('mi_archivo.txt', 'r')
leer = abrir.read()
print(leer)