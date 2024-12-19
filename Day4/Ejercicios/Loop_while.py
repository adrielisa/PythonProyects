monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas - 1 #monedas -=1
else:
    print("No tengo más dinero :( ")

#----------------------------------------------------
respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n)")
else:
    print("Gracias")

#pass----------------------------------------------------
respuesta = 's'

while respuesta == 's':
    pass

print('Hola')
#break----------------------------------------------------
nombre = input("Tu nombre")

for letra in nombre:
    if letra == 'r':
        break
    print(letra)
#continue----------------------------------------------------
nombre = input("Tu nombre")

for letra in nombre:
    if letra == 'r':
        continue
    print(letra)