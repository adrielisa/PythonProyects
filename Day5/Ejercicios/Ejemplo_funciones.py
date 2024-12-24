precios_cafe = [('capuchino', 11.5), ('Expreso', 11.5), ('Moka', 1.9)]

def cafe_mas_caro (lista_precios):

    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in lista_precios: #La primera variable 'cafe' recorrerá los nombres de cafés. La segunda variable 'precio' recorrer los precios del café
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro, precio_mayor)

print(cafe_mas_caro(precios_cafe))

cafe, precio = cafe_mas_caro(precios_cafe)

print(f'El café más caro es {cafe} cuyo precio es: {precio}')