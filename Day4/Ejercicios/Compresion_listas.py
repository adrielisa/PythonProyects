#Sin compresión de listas:
palabra = 'python'
lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

#Con comprensión de listas
palabra = 'python'

lista = [letra for letra in palabra]
print(lista)

#Con comprensión de listas usando números
lista = [n for n in range(0,21,2)]
print(lista)


#Con comprensión de listas usando números, incluso podemos usar un if
lista = [n for n in range(0,21,2) if n * 2 > 10]
print(lista)