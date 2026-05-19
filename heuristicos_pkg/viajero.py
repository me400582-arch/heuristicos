import random
import math

def alet_numero(a, b):
    """Genera un número aleatorio entre a y b"""
    return random.randint(a, b)

def perm_desen_lexi(r, n):
    """Convierte un rango r en una permutación (unranking lexicográfico)"""
    elementos = list(range(n))
    perm = []

    for i in range(n, 0, -1):
        f = math.factorial(i - 1)
        idx = r // f
        r = r % f
        perm.append(elementos.pop(idx))

    return perm

# ========== FUNCIONES 2-OPT ==========

def G(X, i, j, M):
    """Calcula la ganancia de un movimiento 2-opt"""
    n = len(X)
    a, b = X[i], X[(i + 1) % n]
    c, d = X[j], X[(j + 1) % n]
    return M[a][b] + M[c][d] - M[a][c] - M[b][d]

def aplicar_2opt(X, i, j):
    """Aplica un movimiento 2-opt invirtiendo el segmento"""
    return X[:i+1] + X[i+1:j+1][::-1] + X[j+1:]

def ascenso_m_empinado(X, M):
    """
    Mejora una ruta usando ascenso más empinado con 2-opt
    X: ruta (lista de enteros)
    M: matriz de costos
    """
    n = len(X)
    hecho = False

    while not hecho:
        hecho = True
        g_i = 0
        x, y = -1, -1

        for i in range(n - 1):
            for j in range(i + 2, n):
                if i == 0 and j == n - 1:
                    continue

                g_f = G(X, i, j, M)

                if g_f > g_i:
                    g_i = g_f
                    x, y = i, j

        if g_i > 0 and x != -1 and y != -1:
            X = aplicar_2opt(X, x, y)
            hecho = False

    return X

# ========== ALGORITMO PRINCIPAL ==========

def generar_poblacion(tamano_poblacion, n, M):
    """
    Genera una población inicial de rutas mejoradas con 2-opt

    Parámetros:
    - tamano_poblacion: número de individuos
    - n: número de ciudades
    - M: matriz de costos
    """
    P = []
    max_rank = math.factorial(n)

    for i in range(tamano_poblacion):
        # Generar rango aleatorio
        r = alet_numero(0, max_rank - 1)

        # Convertir rango a permutación
        ruta = perm_desen_lexi(r, n)

        # Mejorar la ruta con 2-opt (¡esto es importante!)
        ruta_mejorada = ascenso_m_empinado(ruta, M)

        P.append(ruta_mejorada)

    return P

# ========== FUNCIONES DE COSTO ==========

def calcular_costo(ruta, M):
    """Calcula el costo total de una ruta (circuito hamiltoniano)"""
    costo = 0
    n = len(ruta)
    for i in range(n - 1):
        costo += M[ruta[i]][ruta[i+1]]
    costo += M[ruta[-1]][ruta[0]]
    return costo
