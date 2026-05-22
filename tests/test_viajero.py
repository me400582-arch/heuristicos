import pytest
from unittest.mock import patch

from heuristicos_pkg.viajero import (
    TSP,
    calcular_costo,
    dos_opt,
    generar_matriz_aleatoria,
    generar_poblacion,
)


def test_generar_matriz_aleatoria_simetrica():
    with patch("heuristicos_pkg.viajero.random.randint", return_value=7):
        matriz = generar_matriz_aleatoria(2, simetrica=True)

    assert matriz == [[0, 7], [7, 0]]


def test_generar_matriz_aleatoria_asimetrica():
    with patch("heuristicos_pkg.viajero.random.randint", side_effect=[1, 2]):
        matriz = TSP.generar_matriz_aleatoria(2, simetrica=False)

    assert matriz == [[0, 1], [2, 0]]


def test_generar_ruta():
    matriz = [[0] * 5 for _ in range(5)]
    tsp = TSP(matriz)

    ruta = tsp.generar_ruta(5)

    assert len(ruta) == 5
    assert set(ruta) == set(range(5))


def test_generar_poblacion_instancia():
    matriz = [[0] * 5 for _ in range(5)]
    tsp = TSP(matriz)

    poblacion = tsp.generar_poblacion(10, 5)

    assert len(poblacion) == 10
    for ruta in poblacion:
        assert len(ruta) == 5
        assert set(ruta) == set(range(5))


def test_generar_poblacion_wrapper():
    poblacion = generar_poblacion(7, 4)
    assert len(poblacion) == 7
    for ruta in poblacion:
        assert len(ruta) == 4
        assert set(ruta) == set(range(4))


def test_calcular_costo():
    matriz = [
        [0, 10, 15],
        [10, 0, 20],
        [15, 20, 0],
    ]
    tsp = TSP(matriz)

    assert tsp.calcular_costo([0, 1, 2]) == 45
    assert calcular_costo([0, 1, 2], matriz) == 45


def test_dos_opt_mejora():
    matriz = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    tsp = TSP(matriz)

    ruta = [0, 2, 1, 3]
    costo_inicial = tsp.calcular_costo(ruta)
    nueva_ruta, nuevo_costo = tsp.dos_opt(ruta)

    assert set(nueva_ruta) == set(ruta)
    assert nuevo_costo <= costo_inicial
    assert dos_opt(ruta, matriz) == (nueva_ruta, nuevo_costo)


def test_invalid_matrix():
    with pytest.raises(ValueError):
        TSP([])

    with pytest.raises(ValueError):
        TSP([[0, 1], [1]])


def test_invalid_route():
    matriz = [[0, 1], [1, 0]]
    tsp = TSP(matriz)

    with pytest.raises(ValueError):
        tsp.calcular_costo([0])

    with pytest.raises(ValueError):
        tsp.calcular_costo([0, 0])
