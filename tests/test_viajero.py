import math
from tu_modulo_tsp import (
    alet_numero,
    perm_desen_lexi,
    G,
    aplicar_2opt,
    ascenso_m_empinado,
    generar_poblacion,
    calcular_costo
)

def matriz_ejemplo():
    """Matriz de costos simple (simétrica)"""
    return [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]


def test_perm_desen_lexi():
    n = 4
    r = 5
    perm = perm_desen_lexi(r, n)

    assert len(perm) == n
    assert sorted(perm) == list(range(n))  # debe ser permutación válida


def test_alet_numero():
    a, b = 0, 10
    num = alet_numero(a, b)

    assert a <= num <= b


def test_aplicar_2opt():
    ruta = [0, 1, 2, 3, 4]
    nueva = aplicar_2opt(ruta, 1, 3)

    assert len(nueva) == len(ruta)
    assert sorted(nueva) == sorted(ruta)  # sigue siendo permutación


def test_G_mejora():
    M = matriz_ejemplo()
    ruta = [0, 1, 2, 3]

    ganancia = G(ruta, 0, 2, M)

    assert isinstance(ganancia, (int, float))


def test_calcular_costo():
    M = matriz_ejemplo()
    ruta = [0, 1, 2, 3]

    costo = calcular_costo(ruta, M)

    assert costo > 0


def test_ascenso_m_empinado():
    M = matriz_ejemplo()
    ruta = [0, 2, 1, 3]

    ruta_mejorada = ascenso_m_empinado(ruta, M)

    assert len(ruta_mejorada) == len(ruta)
    assert sorted(ruta_mejorada) == sorted(ruta)

    costo_original = calcular_costo(ruta, M)
    costo_mejorado = calcular_costo(ruta_mejorada, M)

    assert costo_mejorado <= costo_original  # nunca empeora


def test_generar_poblacion():
    M = matriz_ejemplo()
    poblacion = generar_poblacion(5, 4, M)

    assert len(poblacion) == 5

    for ruta in poblacion:
        assert len(ruta) == 4
        assert sorted(ruta) == list(range(4))


def test_poblacion_mejorada():
    M = matriz_ejemplo()
    poblacion = generar_poblacion(3, 4, M)

    for ruta in poblacion:
        costo = calcular_costo(ruta, M)
        assert costo > 0
