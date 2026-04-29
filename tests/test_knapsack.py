from heuristicos_pkg.knapsack import mochila_greedy

def test_mochila_basico():
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidad = 50

    seleccion, valor = mochila_greedy(valores, pesos, capacidad)

    assert valor > 0
    assert sum(pesos[i] for i in seleccion) <= capacidad
si es 
