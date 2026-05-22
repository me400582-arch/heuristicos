import random
import pytest

from heuristicos_pkg.knapsack import (
    generar_instancia_mochila,
    mochila_backtracking,
    mochila_greedy,
    mochila_recocido_simulado,
)


def test_generar_instancia():
    random.seed(1)
    valores, pesos, capacidad = generar_instancia_mochila(n_objetos=5)
    assert len(valores) == 5
    assert len(pesos) == 5
    assert capacidad > 0
    assert all(p > 0 for p in pesos)


def test_generar_instancia_invalida():
    with pytest.raises(ValueError):
        generar_instancia_mochila(n_objetos=0)
    with pytest.raises(ValueError):
        generar_instancia_mochila(valor_min=10, valor_max=5)
    with pytest.raises(ValueError):
        generar_instancia_mochila(peso_min=3, peso_max=2)
    with pytest.raises(ValueError):
        generar_instancia_mochila(capacidad_ratio=0)


def test_mochila_greedy():
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidad = 50
    seleccion, valor = mochila_greedy(valores, pesos, capacidad)
    peso_total = sum(pesos[i] for i in seleccion)
    assert valor > 0
    assert peso_total <= capacidad


def test_mochila_backtracking():
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidad = 50
    valor, peso, seleccion = mochila_backtracking(pesos, valores, capacidad)
    assert peso <= capacidad
    assert valor == 220
    assert seleccion == [0, 1, 1]


def test_mochila_recocido():
    random.seed(7)
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidad = 50
    solucion, valor = mochila_recocido_simulado(valores, pesos, capacidad)
    peso_total = sum(
        pesos[i] for i in range(len(solucion)) if solucion[i] == 1
    )
    assert peso_total <= capacidad
    assert valor >= 0


def test_mochila_recocido_invalidos():
    with pytest.raises(ValueError):
        mochila_recocido_simulado([1], [1], -1)
    with pytest.raises(ValueError):
        mochila_recocido_simulado([1], [1], 1, temperatura=0)
    with pytest.raises(ValueError):
        mochila_recocido_simulado([1], [1], 1, enfriamiento=1.2)
    with pytest.raises(ValueError):
        mochila_recocido_simulado([1], [1], 1, iteraciones=0)


def test_validaciones_basicas():
    with pytest.raises(ValueError):
        mochila_greedy([1, 2], [1], 10)
    with pytest.raises(ValueError):
        mochila_greedy([1, 2], [0, 2], 10)
    with pytest.raises(ValueError):
        mochila_greedy([1, 2], [1, 2], -1)
