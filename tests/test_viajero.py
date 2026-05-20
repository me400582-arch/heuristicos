import pytest
from tsp import TSP


def test_generar_ruta():
    M = [[0]*5 for _ in range(5)]
    tsp = TSP(M)

    ruta = tsp.generar_ruta(5)

    assert len(ruta) == 5
    assert set(ruta) == set(range(5))


def test_generar_poblacion():
    M = [[0]*5 for _ in range(5)]
    tsp = TSP(M)

    poblacion = tsp.generar_poblacion(10, 5)

    assert len(poblacion) == 10

    for ruta in poblacion:
        assert len(ruta) == 5
        assert set(ruta) == set(range(5))


def test_calcular_costo():
    M = [
        [0, 10, 15],
        [10, 0, 20],
        [15, 20, 0]
    ]

    tsp = TSP(M)

    ruta = [0, 1, 2]
    costo = tsp.calcular_costo(ruta)

    # 0->1 (10) + 1->2 (20) + 2->0 (15) = 45
    assert costo == 45


def test_dos_opt_mejora():
    M = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    tsp = TSP(M)

    ruta = [0, 2, 1, 3]

    costo_inicial = tsp.calcular_costo(ruta)
    nueva_ruta, nuevo_costo = tsp.dos_opt(ruta)

    assert set(nueva_ruta) == set(ruta)
    assert nuevo_costo <= costo_inicial
