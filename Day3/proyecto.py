texto = input('Ingrese un texto: ')
texto = texto.lower()

a = input('Ingrese una letra: ')
b = input('Ingrese una letra: ')
c = input('Ingrese una letra: ')
lista = [ ]
lista.append(a)
lista.append(b)
lista.append(c)

# Paso 1 Mostrar cuantas veces aparece cada una de las letras qu eligió
letra1 = texto.count(lista[0])
letra2 = texto.count(lista[1])
letra3 = texto.count(lista[2])
print(f" La letra {a} aparece {letra1} veces")
print(f" La letra {b} aparece {letra2} veces")
print(f" La letra {c} aparece {letra3} veces")

#Paso 2 contar cuántas palabras hay a lo largo de todo el texto
def contar_palabras(texto):
    palabras = texto.split()  # Divide el texto en palabras usando espacios
    return len(palabras)  # Cuenta el número de palabras

cantidad_palabras = contar_palabras(texto)
if cantidad_palabras > 1:
    print(f"El texto tiene {cantidad_palabras} palabras")

else:
    print(f"El texto tiene {cantidad_palabras} palabra")

#Paso 3 Informar la primera y última letra del texto
primera = texto[0]
ultima = texto[-1]

print(f"Primera letra del texto: {primera} y última letra del texto: {ultima}")

#Paso 4 Mostrar el texto con el orden de palabras invertidos
palabras = texto.split()
palabras_invertidas = palabras[::-1]
texto_invertido = " ".join(palabras_invertidas)
print(f"El texto con el orden de palabras inveridas es: {texto_invertido}")

#Paso 5 Verificar si la palabra "Python" existe en el texto
ispython = "python" in texto

if ispython == True :
    print("Su texto tiene la palabra Python")

else:
    print("su texto no tiene la palabra Pyhton")