"""
Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.
"""

puntos_anteriores = 875
puntos_nuevos = 350

print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos, puntos_anteriores + puntos_nuevos))