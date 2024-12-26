"""
El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie
de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno
deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a
mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en
la palabra oculta, pierde una vida

Tiene seis vidas y se las iremos descontando de una
en una, cada vez que el jugador elija una letra incorrecta.
Si se agotan las vidas antes de adivinar la palabra, el jugador pierde. Pero si adivina la palabra
completa antes de perder todas las vidas, el jugador gana. 

"""
from random import choice

def inicializar_juego():
    palabras = ['brisa', 'aire', 'playa', 'amor', 'felicidad']
    palabra = choice(palabras)
    letras_adivinadas = set()  # Conjunto para almacenar letras ya elegidas
    vidas = 6
    return palabra, letras_adivinadas, vidas

def mostrar_tablero(palabra, letras_adivinadas):
    """Muestra el estado actual del juego"""
    resultado = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += '_'
    return ' '.join(resultado)

def elegir_letra():
    while True:
        letra = input('Ingrese una letra: ').lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        print('Por favor, ingrese una única letra válida.')

def jugar():
    palabra, letras_adivinadas, vidas = inicializar_juego()
    palabra_completa = set(palabra)  # Conjunto de letras únicas en la palabra
    
    print("¡Bienvenido al juego del Ahorcado!")
    
    while vidas > 0:
        print(f"\nVidas restantes: {vidas}")
        print(f"Palabra: {mostrar_tablero(palabra, letras_adivinadas)}")
        
        letra = elegir_letra()
        
        if letra in letras_adivinadas:
            print("Ya elegiste esa letra. Intenta con otra.")
            continue
            
        letras_adivinadas.add(letra)
        
        if letra in palabra:
            print("¡Correcto!")
            if palabra_completa.issubset(letras_adivinadas):
                print(f"\n¡Felicitaciones! ¡Ganaste! La palabra era: {palabra}")
                return
        else:
            vidas -= 1
            print("Letra incorrecta.")
            
    print(f"\n¡Game Over! La palabra era: {palabra}")

if __name__ == "__main__":
    jugar()