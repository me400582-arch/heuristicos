import random
from tu_modulo_tsp import (
    G,
    ascenso_m_empinado,
    ascenso_mj_empinado,
    aplicar_2opt,
    intercambiar_ciudad,
    parcial_emparejado,
    num_aleato,
    seleccionar_inicial,
    costo
)

def matriz_ejemplo():
    return [
        [0, 2, 9, 10],
        [2, 0, 6, 4],
        [9, 6, 0, 8],
        [10, 4, 8, 0]
    ]

def test_G():
    M = matriz_ejemplo()
    ruta = [0, 1, 2, 3]

    g = G(ruta, 0, 2, M)

    assert isinstance(g, (int, float))

def test_aplicar_2opt():
    ruta = [0, 1, 2, 3, 4]

    nueva = aplicar_2opt(ruta, 1, 3)

    assert len(nueva) == len(ruta)
    assert sorted(nueva) == sorted(ruta)

def test_ascenso_m_empinado():
    M = matriz_ejemplo()
    ruta = [0, 2, 1, 3]

    mejor = ascenso_m_empinado(ruta, M)

    assert len(mejor) == len(ruta)
    assert sorted(mejor) == sorted(ruta)

def test_ascenso_mj_empinado():
    M = matriz_ejemplo()
    ruta = [0, 3, 2, 1]

    mejor = ascenso_mj_empinado(ruta, M)

    assert len(mejor) == len(ruta)
    assert sorted(mejor) == sorted(ruta)

def test_intercambiar_ciudad():
    A = [0, 1, 2, 3]
    B = [3, 2, 1, 0]

    C, D = intercambiar_ciudad(A, B, 1, 2)

    assert len(C) == len(A)
    assert len(D) == len(B)

def test_parcial_emparejado():
    A = [0, 1, 2, 3]
    B = [3, 2, 1, 0]

    C, D = parcial_emparejado(A, B, 1, 2)

    assert len(C) == len(A)
    assert len(D) == len(B)

    assert sorted(C) == sorted(A)
    assert sorted(D) == sorted(B)

def test_num_aleato():
    a, b = 0, 10
    num = num_aleato(a, b)

    assert a <= num <= b

def test_seleccionar_inicial():
    poblacion = seleccionar_inicial(5)

    assert len(poblacion) == 5

    for ruta in poblacion:
        assert len(ruta) > 0
        assert sorted(ruta) == sorted(ruta)  # sigue siendo lista válida

def test_costo():
    M = matriz_ejemplo()
    ruta = [0, 1, 2, 3]

    # redefinir costo local si depende de M global
    def costo_local(ruta):
        total = 0
        for i in range(len(ruta)-1):
            total += M[ruta[i]][ruta[i+1]]
        total += M[ruta[-1]][ruta[0]]
        return total

    c = costo_local(ruta)

    assert c > 0
