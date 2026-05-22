import pytest
from heuristicos_pkg.knapsack import (
    generar_instancia_mochila,
    mochila_greedy,
    mochila_backtracking,
    mochila_recocido_simulado,
)

# TEST GENERADOR DE INSTANCIAS

def test_generar_instancia():

    valores, pesos, capacidad = generar_instancia_mochila(
        n_objetos=5
    )

    assert len(valores) == 5

    assert len(pesos) == 5

    assert capacidad > 0

# TEST GREEDY

def test_mochila_greedy():

    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidad = 50

    seleccion, valor = mochila_greedy(
        valores,
        pesos,
        capacidad
    )

    peso_total = sum(
        pesos[i]
        for i in seleccion
    )

    assert valor > 0

    assert peso_total <= capacidad

# TEST BACKTRACKING

def test_mochila_backtracking():

    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidad = 50

    valor, peso, seleccion = mochila_backtracking(
        pesos,
        valores,
        capacidad
    )

    assert peso <= capacidad

    assert valor == 220

# TEST RECOCIDO SIMULADO

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
def test_capacidad_negativa():

    with pytest.raises(ValueError):

        mochila_greedy(
            [1, 2],
            [1, 2],
            -1
        )


def test_pesos_invalidos():

    with pytest.raises(ValueError):

        mochila_greedy(
            [1, 2],
            [0, 2],
            10
        )


def test_tamanos_distintos():

    with pytest.raises(ValueError):

        mochila_greedy(
            [1],
            [1, 2],
            10
        )
