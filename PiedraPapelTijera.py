import random

def jugar():
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel o 'ti' para tijera. \n").lower()
    computadora = random.choice(['pi','pa','ti'])
    print(f'La computadora eligio: {computadora}')
    if usuario == computadora:
        return '¡Empate!'

    if ganoElJugador(usuario,computadora):
        return '!Ganaste¡'
    
    return '¡Perdiste!'


def ganoElJugador(jugador,oponente):
    #Retorna True (verdadero) si gana el jugador
    #Piedra gana a tijera
    #Tijera gana a papel
    #Papel gana a Piedra
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())
    
