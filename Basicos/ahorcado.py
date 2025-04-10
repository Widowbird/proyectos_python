import random
import string

from palabras import palabras
from ahorcadoDiagrama import vidas_diccionario_visual


def obtenerPalabraValida(listaPalabras):
    #Seleccionar una palabra al azar de la lista de palabras validas
    palabra = random.choice(listaPalabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(listaPalabras)
        
    return palabra.upper()

def ahorcado():
    print('=================================')
    print('¡Bienvenido(a) al juego El Ahorcado!')
    print('=================================')

    palabra = obtenerPalabraValida(palabras)
    letrasPorAdivinar = set(palabra)
    abecedario = set(string.ascii_uppercase)
    letrasAdivinadas = set()

    vidas = 7

    while len(letrasPorAdivinar)>0 and vidas >0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letrasAdivinadas)}")

        #Mostrar el estado actual de la palabra
        palabraLista = [letra if letra in letrasAdivinadas
                        else '_' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabraLista)}")

        letraUsuario = input("Escoge una letra: ").upper()

        #Si la letra escogida por el usuario esta en el abecedario
        #y no esta en el conjunto de letras que ya han ingresado,
        #se añade la letra la conjunto de letras ingresadas
        if letraUsuario in abecedario - letrasAdivinadas:
            letrasAdivinadas.add(letraUsuario)

            #Si la letra está en la palabra o no
            #Si no, quitamos una vida
            if letraUsuario in letrasPorAdivinar:
                letrasPorAdivinar.remove(letraUsuario)
                print('')
            else:
                vidas -= 1
                print(f"\nTu letra {letraUsuario} mo está en la palabra.")
        #Si la letra escogida por el usuario ya fue ingresada
        elif letraUsuario in letrasAdivinadas:
            print('\nYa escogiste esa letra, por favor, elige una nueva letra')
        else:
            print("\nEsta leta no es valida")

    #El juego llega  aesta linea cuando se adivinan todas las letras de la palabra
    #o cuando se agotan las vidas del jugador
    if vidas == 0:
        print(vidasDiccionarioVisual[vidas])
        print(f'¡Ahorcado! lo lamento mucho. La palabra era: {palabra}')
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')


ahorcado()
