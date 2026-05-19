import random
import math

# =========================
# 2-OPT
# =========================

def G(X, i, j, M):
    n = len(X)
    a, b = X[i], X[(i + 1) % n]
    c, d = X[j], X[(j + 1) % n]
    return (M[a][b] + M[c][d]) - (M[a][c] + M[b][d])


def aplicar_2opt(X, i, j):
    return X[:i+1] + X[i+1:j+1][::-1] + X[j+1:]


def ascenso_m_empinado(X, M):
    n = len(X)

    while True:
        mejora = 0
        mejor_i, mejor_j = -1, -1

        for i in range(n - 1):
            for j in range(i + 2, n):
                if i == 0 and j == n - 1:
                    continue

                ganancia = G(X, i, j, M)

                if ganancia > mejora:
                    mejora = ganancia
                    mejor_i, mejor_j = i, j

        if mejora > 0:
            X = aplicar_2opt(X, mejor_i, mejor_j)
        else:
            break

    return X


# =========================
# CRUCE (PMX)
# =========================

def parcial_emparejado(A, B, inicio, fin):
    n = len(A)
    C = [None] * n
    D = [None] * n

    for i in range(inicio, fin + 1):
        C[i] = A[i]
        D[i] = B[i]

    def rellenar(hijo, padre, seg1, seg2):
        for i in range(n):
            if hijo[i] is None:
                val = padre[i]
                while val in hijo:
                    idx = seg1.index(val)
                    val = seg2[idx]
                hijo[i] = val

    rellenar(C, B, A, B)
    rellenar(D, A, B, A)

    return C, D


# =========================
# GENÉTICO
# =========================

def calcular_costo(ruta, M):
    return sum(M[ruta[i]][ruta[(i + 1) % len(ruta)]] for i in range(len(ruta)))


def generar_poblacion(tamano, n, M):
    P = []
    for _ in range(tamano):
        ruta = list(range(n))
        random.shuffle(ruta)
        ruta = ascenso_m_empinado(ruta, M)
        P.append(ruta)
    return P


def algoritmo_genetico(n_poblacion, generaciones, M,
                      prob_cruce=0.9,
                      prob_mutacion=0.1):

    n = len(M)
    P = generar_poblacion(n_poblacion, n, M)

    def seleccionar(P):
        a, b = random.sample(P, 2)
        return a if calcular_costo(a, M) < calcular_costo(b, M) else b

    mejor = min(P, key=lambda x: calcular_costo(x, M))

    for _ in range(generaciones):
        nuevos = []

        while len(nuevos) < n_poblacion:
            padre1 = seleccionar(P)
            padre2 = seleccionar(P)

            if random.random() < prob_cruce:
                i = random.randint(0, n-2)
                j = random.randint(i+1, n-1)
                hijo1, hijo2 = parcial_emparejado(padre1, padre2, i, j)
            else:
                hijo1, hijo2 = padre1[:], padre2[:]

            # mutación
            if random.random() < prob_mutacion:
                i, j = random.sample(range(n), 2)
                hijo1[i], hijo1[j] = hijo1[j], hijo1[i]

            nuevos.append(hijo1)

        P = sorted(P + nuevos, key=lambda x: calcular_costo(x, M))[:n_poblacion]

        if calcular_costo(P[0], M) < calcular_costo(mejor, M):
            mejor = P[0]

    return mejor
