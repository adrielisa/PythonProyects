texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5] #Extrae del índice 2 hasta el 4 (Deja de extraer justo antes de llegar al 5)
print(fragmento)

texto1 = "ABCDEFGHIJKLM"
fragmento1 = texto1[2:] #Extrae del índice 2 hasta el último
print(fragmento1)


texto2 = "ABCDEFGHIJKLM"
fragmento2 = texto2[:5] #Extrae del inicio hasta el índice 5
print(fragmento2)

texto3 = "ABCDEFGHIJKLM"
fragmento3 = texto3[2:10:2] #Extrae desde el índice 2 hasta el 10 dando saltos de 2 en 2
print(fragmento3)