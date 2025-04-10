import random

def adivinaElNumero(x):
    print("========================")
    print("¡Bienvenido(a) al juego!")
    print("========================")
    print("Tu meta es adivinar el número generado por la computadora")

    numeroAleatorio = random.randint(1,x) #Numero aleatorio entre 1 y x.

    prediccion = 0

    while prediccion != numeroAleatorio:
        #El usuario agrega u numero
        prediccion = int(input(f"Advina un número entre 1 y {x}: "))

        if prediccion < numeroAleatorio:
            print("Intenta otra vez. Este numero es muy pequeño")
        elif prediccion > numeroAleatorio:
            print("Intenta otra vez. Este numero es muy grande")

    print(f"¡Felciitaciones, adivinaste el numero {numeroAleatorio} correctamente")

adivinaElNumero(10)    
