"""
La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
número y el programa puede responder cuatro cosas distintas:
 Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
un número que no está permitido.
 Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
 Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
misma manera.
 Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
intentos le ha tomado. 

"""

from random import *

nombre = input('¿Cuál es tu nombre?: ')
(print(f'Hola {nombre}, he pensado un numero entre el 1 y 100, tienes solo 8 intentos para adivinar cual es el número'))
numero_usuario = int(input('Ingrese un número: '))
numero_programa = randint(1,101)
intento = 8

while intento > 0:
    if numero_usuario < 1 or numero_usuario > 100:
        print('Número no permitido')
        intento = intento - 1
        print(f'Le quedan {intento} intentos')
        numero_usuario = int(input('Ingrese un número: '))
    elif numero_usuario < numero_programa:
        print('Respuesta incorrecta, número mayor')
        intento = intento - 1
        print(f'Le quedan {intento} intentos')
        numero_usuario = int(input('Ingrese un número: '))
    elif numero_usuario > numero_programa:
        print('Respueta incorrecta. número menor')
        intento = intento - 1
        print(f'Le quedan {intento} intentos')
        numero_usuario = int(input('Ingrese un número: '))
    elif numero_programa == numero_usuario:
        print('Has ganado')
        break