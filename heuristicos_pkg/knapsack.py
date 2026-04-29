def mochila_greedy(valores, pesos, capacidad):
    n = len(valores)
    indices = list(range(n))

    # ordenar por valor/peso
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
