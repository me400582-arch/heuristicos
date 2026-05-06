from heuristicos_pkg.knapsack import mochila_greedy, mochila_backtracking

def test_mochila_greedy():
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidad = 50

    seleccion, valor = mochila_greedy(valores, pesos, capacidad)

    assert valor > 0
    assert sum(pesos[i] for i in seleccion) <= capacidad


def test_mochila_backtracking():
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidad = 50

    valor, peso, seleccion = mochila_backtracking(pesos, valores, capacidad)

    assert peso <= capacidad
    assert valor == 220

from heuristicos_pkg.knapsack import mochila_recocido_simulado

def test_mochila_recocido():
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidad = 50

    solucion, valor = mochila_recocido_simulado(
        valores,
        pesos,
        capacidad
    )

    peso_total = sum(
        pesos[i]
        for i in range(len(solucion))
        if solucion[i] == 1
    )

    assert peso_total <= capacidad
    assert valor > 0
