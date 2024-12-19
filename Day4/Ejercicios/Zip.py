#zip sirve para combinar el contenido de 2 listas

nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,42]
ciudades = ['Lima', 'Madrid', 'Mexico']
combinados = list(zip(nombres,edades,ciudades))

for nombre, edad, ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')