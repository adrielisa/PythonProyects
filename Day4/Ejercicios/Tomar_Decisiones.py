mascota = 'Gato'

if mascota == 'Gato':
    print('Tienes un gato')
elif mascota == 'Perro':
    print('Tienes un perro')
elif mascota == 'Pez':
    print('Tienes un pez')
else:
    print('No sé que animal tienes')

edad = 16
calificacion = 9

if edad < 18:
    print('Eres menor de edad')
    if calificacion >=7:
        print('Aprobado')
    else:
        print('Reprobado')
else: 
    print('Eres un adulto')