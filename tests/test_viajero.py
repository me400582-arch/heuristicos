from heuristicos_pkg.viajero import (
    perm_desen_lexi,
    aplicar_2opt,
    calcular_costo,
    generar_poblacion,
    ascenso_m_empinado
)

def test_perm_desen_lexi():
    perm = perm_desen_lexi(5, 4)

    assert len(perm) == 4
    assert sorted(perm) == [0, 1, 2, 3]


def test_aplicar_2opt():
    ruta = [0, 1, 2, 3, 4]

    nueva = aplicar_2opt(ruta, 1, 3)

    assert nueva != ruta
    assert sorted(nueva) == sorted(ruta)


def test_calcular_costo():
    M = [
        [0, 10, 15],
        [10, 0, 20],
        [15, 20, 0]
    ]

    ruta = [0, 1, 2]

    costo = calcular_costo(ruta, M)

    assert costo == 45


def test_generar_poblacion():
    M = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    poblacion = generar_poblacion(5, 4, M)

    assert len(poblacion) == 5

    for ruta in poblacion:
        assert len(ruta) == 4
        assert sorted(ruta) == [0, 1, 2, 3]


def test_ascenso_m_empinado():
    M = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    ruta = [0, 2, 1, 3]

    nueva = ascenso_m_empinado(ruta, M)

    assert len(nueva) == 4
    assert sorted(nueva) == [0, 1, 2, 3]
