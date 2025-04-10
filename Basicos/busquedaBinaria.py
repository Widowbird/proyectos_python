import random
import time


def busquedaIngenua(lista,objetivo):
    for i in range(len(lista)):
        #Vamos por cada indice de la lista
        if lista[i] == objetivo:
            return i
    return -1


def busquedaBinaria(lista,objetivo,limiteInferior = None,limiteSuperior = None):
    if limiteInferior is None:
        limiteInferior = 0
    if limiteSuperior is None:
        limiteSuperior = len(lista) - 1

    if limiteSuperior < limiteInferior:
        return -1
    
    puntoMedio = (limiteInferior + limiteSuperior) // 2

    if lista[puntoMedio] == objetivo:
        return puntoMedio
    elif objetivo < lista[puntoMedio]:
        return busquedaBinaria(lista,objetivo,limiteInferior,puntoMedio - 1)
    else:
        return busquedaBinaria(lista,objetivo,puntoMedio + 1,limiteSuperior)
        


if __name__=='__main__':
    tamaño = 10000
    conjunto_inicial = set()

    while len(conjunto_inicial)<tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño,3*tamaño))

    lista_ordenada = sorted(list(conjunto_inicial))

    #Medi tiempo de busqueda ingenua
    inicio = time.time()
    for objetivo in lista_ordenada:
        busquedaIngenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua: {fin -inicio} segundos")

    #Medir el tiempo busqueda binaria
    inicio = time.time()
    for objetivo in lista_ordenada:
        busquedaBinaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda bineria: {fin-inicio} segundo")
         
