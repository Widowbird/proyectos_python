import random

def adivinaElNumeroComputadora(x):
    print("=====================")
    print("¡Bienvenido al juego!")
    print("=====================")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo...")

    limiteInferior = 1
    limiteSuperior = x

    respuesta = ""

    while respuesta != "c":
        #Predicción
        if limiteInferior != limiteSuperior:
            prediccion = random.randint(limiteInferior,limiteSuperior)
        else:
            predicción = limiteInferior

        #Obtener respuesta
        respuesta = input(f"""Mi predicción es: {prediccion}. Si es muy alta ingresa A. Si es muy baja ingresa B. Si es correcta. ingresa C: """).lower()

        if respuesta == "a":
            limiteSuperior = prediccion - 1
            #Intervalo inicial : [1,10]
            #Prediccion: 6
            #Respuesta: "a"
            #Respuesta: [1,5]
        elif respuesta == "b":
            limiteInferior = prediccion + 1
    
    print(f"""¡Siii¡ La computadora adivinó tu numero correctamente: {prediccion}""")

adivinaElNumeroComputadora(10)
