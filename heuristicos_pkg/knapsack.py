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
