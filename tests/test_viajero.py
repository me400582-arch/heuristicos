import math
import random
from tu_modulo_tsp import (
    G,
    aplicar_2opt,
    ascenso_m_empinado,
    ascenso_mas_empinado,
    ascenso_mj_empinado,
    intercambiar_ciudad,
    parcial_emparejado,
    num_aleato,
    alet_numero,
    perm_desen_lexi,
    generar_poblacion,
    calcular_costo,
    tsp
)

# ---------- MATRIZ SIMPLE ----------
def matriz_ejemplo():
    return [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]


# ---------- TEST G ----------
def G():
    M = matriz_ejemplo()
    ruta = [0, 1, 2, 3]

    g = G(ruta, 0, 2, M)

    assert isinstance(g, (int, float))


# ---------- TEST aplicar_2opt ----------
def aplicar_2opt():
    ruta = [0, 1, 2, 3, 4]

    nueva = aplicar_2opt(ruta, 1, 3)

    assert len(nueva) == len(ruta)
    assert sorted(nueva) == sorted(ruta)


# ---------- TEST ascenso_m_empinado (versión con M) ----------
def ascenso_m_empinado():
    M = matriz_ejemplo()
    ruta = [0, 2, 1, 3]

    nueva = ascenso_m_empinado(ruta, M)

    assert len(nueva) == len(ruta)
    assert sorted(nueva) == sorted(ruta)


# ---------- TEST ascenso_mas_empinado ----------
def ascenso_mas_empinado():
    M = matriz_ejemplo()
    ruta = [0, 3, 2, 1]

    nueva = ascenso_mas_empinado(ruta, M)

    assert len(nueva) == len(ruta)
    assert sorted(nueva) == sorted(ruta)


# ---------- TEST ascenso_mj_empinado ----------
def ascenso_mj_empinado():
    M = matriz_ejemplo()
    ruta = [0, 3, 1, 2]

    nueva = ascenso_mj_empinado(ruta, M)

    assert len(nueva) == len(ruta)
    assert sorted(nueva) == sorted(ruta)


# ---------- TEST intercambiar_ciudad ----------
def intercambiar_ciudad():
    A = [0, 1, 2, 3]
    B = [3, 2, 1, 0]

    C, D = intercambiar_ciudad(A, B, 1, 2)

    assert len(C) == len(A)
    assert len(D) == len(B)


# ---------- TEST parcial_emparejado ----------
def parcial_emparejado():
    A = [0, 1, 2, 3]
    B = [3, 2, 1, 0]

    C, D = parcial_emparejado(A, B, 1, 2)

    assert len(C) == len(A)
    assert len(D) == len(B)

    # Deben seguir siendo permutaciones válidas
    assert sorted(C) == sorted(A)
    assert sorted(D) == sorted(B)


# ---------- TEST num_aleato ----------
def num_aleato():
    a, b = 0, 10
    num = num_aleato(a, b)

    assert a <= num <= b


# ---------- TEST alet_numero ----------
def alet_numero():
    a, b = 0, 10
    num = alet_numero(a, b)

    assert a <= num <= b


# ---------- TEST perm_desen_lexi ----------
def perm_desen_lexi():
    n = 4
    r = 5

    perm = perm_desen_lexi(r, n)

    assert len(perm) == n
    assert sorted(perm) == list(range(n))


# ---------- TEST generar_poblacion ----------
def generar_poblacion():
    M = matriz_ejemplo()

    poblacion = generar_poblacion(5, 4, M)

    assert len(poblacion) == 5

    for ruta in poblacion:
        assert len(ruta) == 4
        assert sorted(ruta) == list(range(4))


# ---------- TEST calcular_costo ----------
def calcular_costo():
    M = matriz_ejemplo()
    ruta = [0, 1, 2, 3]

    costo = calcular_costo(ruta, M)

    assert costo > 0


# ---------- TEST tsp (cruce) ----------
def tsp():
    M = matriz_ejemplo()

    A = [0, 1, 2, 3]
    B = [3, 2, 1, 0]

    C, D = tsp(A, B, M)

    assert len(C) == len(A)
    assert len(D) == len(B)

    assert sorted(C) == sorted(A)
    assert sorted(D) == sorted(B)
