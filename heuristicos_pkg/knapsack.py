def mochila_greedy(valores, pesos, capacidad):
    """
    Algoritmo greedy para el problema de la mochila.
    Ordena por valor/peso y selecciona mientras haya espacio.
    """
    n = len(valores)
    indices = list(range(n))

    indices.sort(key=lambda i: valores[i]/pesos[i], reverse=True)

    total_valor = 0
    peso_actual = 0
    seleccion = []

    for i in indices:
        if peso_actual + pesos[i] <= capacidad:
            seleccion.append(i)
            peso_actual += pesos[i]
            total_valor += valores[i]

    return seleccion, total_valor


def mochila_backtracking(pesos, valores, capacidad):
    """
    Solución óptima usando backtracking (fuerza bruta).
    """
    n = len(pesos)
    best = [0, 0, []]

    def bt(idx, current):
        if idx == n:
            peso = sum(pesos[i] * current[i] for i in range(n))
            valor = sum(valores[i] * current[i] for i in range(n))

            if peso <= capacidad and valor > best[0]:
                best[0] = valor
                best[1] = peso
                best[2] = current[:]
            return

        # elegir objeto
        current.append(1)
        bt(idx + 1, current)
        current.pop()

        # no elegir objeto
        current.append(0)
        bt(idx + 1, current)
        current.pop()

    bt(0, [])
    return best

import random
import math


def mochila_recocido_simulado(valores, pesos, capacidad,
                               T0=1000,
                               alpha=0.999,
                               iteraciones=5000):
    """
    Algoritmo de recocido simulado para el problema de la mochila.
    """

    n = len(valores)

    # solución inicial
    X = [0] * n

    peso_actual = 0
    valor_actual = 0

    mejor_X = X[:]
    mejor_valor = 0

    T = T0

    for _ in range(iteraciones):

        # elegir índice aleatorio
        j = random.randint(0, n - 1)

        Y = X[:]

        # cambiar bit
        Y[j] = 1 - Y[j]

        nuevo_peso = peso_actual
        nuevo_valor = valor_actual

        # si agregamos objeto
        if Y[j] == 1:
            nuevo_peso += pesos[j]
            nuevo_valor += valores[j]

        # si quitamos objeto
        else:
            nuevo_peso -= pesos[j]
            nuevo_valor -= valores[j]

        # verificar factibilidad
        if nuevo_peso <= capacidad:

            delta = nuevo_valor - valor_actual

            # mejora
            if delta > 0:
                X = Y
                peso_actual = nuevo_peso
                valor_actual = nuevo_valor

            # aceptar peor solución con probabilidad
            else:
                prob = math.exp(delta / T)

                if random.random() < prob:
                    X = Y
                    peso_actual = nuevo_peso
                    valor_actual = nuevo_valor

            # actualizar mejor solución
            if valor_actual > mejor_valor:
                mejor_valor = valor_actual
                mejor_X = X[:]

        # enfriamiento
        T *= alpha

    return mejor_X, mejor_valor
