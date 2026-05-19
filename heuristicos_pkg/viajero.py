
import random
"Este codigo Ganancia en de un movimiento 2-opt"

def G (X, i, j, M): # Se define función G, X es la ruta,
                    # i y j son las posiciones donde se corta la ruta
    n = len(X)      # M es la distcia o los costos. "n" guarda el tamaño de X

    a = X[i]
    b = X[(i + 1) % n] #%n es modulo si llega al final, empieza otra vez en inicio
    c = X[j]
    d = X[(j + 1) % n]

    return M[a][b] + M[c][d] - M[a][c] - M[b][d] # Aplica la ganancia

"Ascenso más empinado con 2-opt"
def ascenso_m_empinado (X, i, j): # Definicmos la función
    return X[:i+1] + X[i+1:j+1][::-1] + X[j+1:]
          # :i+1 toma los elementos desdee el inicio hasta la posicion i
          # i+1:j+1 Toma un inicio y un final es decir i y j
          # ::-1 Inicio todo, fin todo, paso hacia atras (-1) un orden inverso
          # j+1 Tona una posicion j + 1 hasta el final

"Se mejora el ascenso más empinado con 2-opt"
def ascenso_mj_empinado(X, M): #Toma X como la ruta y M como el costo
    n = len(X)
    hecho = False  # todavia hay trabajo por hacer

    while not hecho: # ya no hay nada que mejorar
        hecho = True
        g_i = 0 # Guarda la mejor ganancia encontrada hasta ahora
        x, y = -1, -1  # x = i, y = j el (-1) significa no se ha encontrado
                       # un movimiento  bueno

        for i in range(0, n - 1): # se crea un ciclo i que va de 0 hasta n - 1
            for j in range(i + 2, n): # Empieza desde i + 2 hasta n

                # evitar romper el ciclo (opcional)
                if i == 0 and j == n - 1:
                    continue

                g_f = G (X, i, j, M) # g_f es el nuevo costo con la nueva ruta

                if g_f > g_i: # g_f es mas grande que g_i
                    g_i = g_f
                    x = i
                    y = j

        if g_i > 0: # la ganancia inicial es mayor qu cero
            X = ascenso_m_empinado(X, x, y)
            hecho = False

    return X

"Es un intercambio de rutas"

def intercambiar_ciudad(alpha, beta, j, k): # α y β son listas y j,k son indices
    gamma = alpha.copy() # γ y δ son rutas origiales
    delta = beta.copy() #  genera copias α, β lo cual son copias independientes

    for i in range(j, k + 1): # se crea un ciclo, empieza desde j hasta k
        gamma[i], delta[i] = delta[i], gamma[i] # Intercambiar γ_i y δ_i,

    return gamma, delta

import random

def num_aleato(a, b):
    return random.randint(a, b)

def parcial_emparejado(A, B, inicio, fin):
    n = len(A)
    C = [None] * n
    D = [None] * n

    # Copiar segmentos
    for i in range(inicio, fin + 1):
        C[i] = A[i]
        D[i] = B[i]

    def rellenar(hijo, padre_actual, segmento_copiado, otro_segmento):
        for i in range(n):
            if hijo[i] is None:
                val = padre_actual[i]
                # Si el valor ya está en el hijo, seguimos el mapeo
                while val in hijo:
                    # Buscamos el valor en el segmento que ya copiamos
                    idx = segmento_copiado.index(val)
                    val = otro_segmento[idx]
                hijo[i] = val

    # Para C: usamos valores de B, pero mapeamos contra el segmento de A
    rellenar(C, B, A, B)
    # Para D: usamos valores de A, pero mapeamos contra el segmento de B
    rellenar(D, A, B, A)

    return C, D

def G(X, i, j, M):
    n = len(X)
    a, b = X[i], X[(i + 1) % n]
    c, d = X[j], X[(j + 1) % n]
    # Ganancia = Distancia actual - Distancia nueva
    return (M[a][b] + M[c][d]) - (M[a][c] + M[b][d])

def aplicar_2opt(X, i, j):
    # Invierte el segmento entre i+1 y j
    return X[:i+1] + X[i+1:j+1][::-1] + X[j+1:]

def ascenso_mas_empinado(X, M):
    n = len(X)
    hecho = False
    while not hecho:
        hecho = True
        g_mejor = 0
        movimiento = None

        for i in range(n - 1):
            for j in range(i + 2, n):
                if i == 0 and j == n - 1: continue

                ganancia = G(X, i, j, M)
                if ganancia > g_mejor:
                    g_mejor = ganancia
                    movimiento = (i, j)

        if g_mejor > 0:
            X = aplicar_2opt(X, movimiento[0], movimiento[1])
            hecho = False
    return X

def tsp(A, B, M):
    n = len(A)
    # h es la longitud del segmento, j es el inicio
    h = num_aleato(2, n // 2)
    j = num_aleato(0, n - h - 1)
    fin = j + h

    C, D = parcial_emparejado(A, B, j, fin)

    C = ascenso_mas_empinado(C, M)
    D = ascenso_mas_empinado(D, M)

    return C, D

    def calcular_costo(ruta, matriz):
    total = 0
    n = len(ruta)
    for i in range(n):
        total += matriz[ruta[i]][ruta[(i + 1) % n]]
    return total

print(f"Costo Padre 1: {calcular_costo(padre_1, M)}")
print(f"Costo Hijo A: {calcular_costo(hijo_a, M)}")

import random

# Configuración inicial
random.seed(42)

# Parámetros
n_poblacion = 20
c_max_ite = 100
n_ciudades = 20

# Matriz de costos (ejemplo)
M = [[0]*n_ciudades for _ in range(n_ciudades)]
for i in range(n_ciudades):
    for j in range(i+1, n_ciudades):
        costo = random.randint(10, 99)
        M[i][j] = costo
        M[j][i] = costo

# Función para generar población inicial
def seleccionar_inicial(tam):
    poblacion = []
    for _ in range(tam):
        ruta = list(range(n_ciudades))
        random.shuffle(ruta)
        # Aplicar mejora inicial (opcional)
        # ruta = ascenso_mas_empinado(ruta, M)
        poblacion.append(ruta)
    return poblacion

# Función de costo
def costo(ruta):
    total = 0
    for i in range(len(ruta)-1):
        total += M[ruta[i]][ruta[i+1]]
    total += M[ruta[-1]][ruta[0]]
    return total

# --- Helper functions for tsp (from cell gZusWbo2w7JT) ---
def num_aleato(a, b):
    return random.randint(a, b)

def parcial_emparejado(A, B, inicio, fin):
    n = len(A)
    C = [None] * n
    D = [None] * n

    # Copiar segmentos
    for i in range(inicio, fin + 1):
        C[i] = A[i]
        D[i] = B[i]

    def rellenar(hijo, padre_actual, segmento_copiado, otro_segmento):
        for i in range(n):
            if hijo[i] is None:
                val = padre_actual[i]
                # Si el valor ya está en el hijo, seguimos el mapeo
                while val in hijo:
                    # Buscamos el valor en el segmento que ya copiamos
                    idx = segmento_copiado.index(val)
                    val = otro_segmento[idx]
                hijo[i] = val

    # Para C: usamos valores de B, pero mapeamos contra el segmento de A
    rellenar(C, B, A, B)
    # Para D: usamos valores de A, pero mapeamos contra el segmento de B
    rellenar(D, A, B, A)

    return C, D

def G(X, i, j, M_arg):
    n = len(X)
    a, b = X[i], X[(i + 1) % n]
    c, d = X[j], X[(j + 1) % n]
    # Ganancia = Distancia actual - Distancia nueva
    return (M_arg[a][b] + M_arg[c][d]) - (M_arg[a][c] + M_arg[b][d])

def aplicar_2opt(X, i, j):
    # Invierte el segmento entre i+1 y j
    return X[:i+1] + X[i+1:j+1][::-1] + X[j+1:]

def ascenso_mas_empinado(X, M_arg):
    n = len(X)
    hecho = False
    while not hecho:
        hecho = True
        g_mejor = 0
        movimiento = None

        for i in range(n - 1):
            for j in range(i + 2, n):
                if i == 0 and j == n - 1: continue

                ganancia = G(X, i, j, M_arg)
                if ganancia > g_mejor:
                    g_mejor = ganancia
                    movimiento = (i, j)

        if g_mejor > 0:
            X = aplicar_2opt(X, movimiento[0], movimiento[1])
            hecho = False
    return X
# --- End of Helper functions ---


# Tu función de cruce (tsp) - FULL IMPLEMENTATION
def tsp(A, B):
    # M is globally accessible in this cell
    n = len(A)
    # h es la longitud del segmento, j es el inicio
    h = num_aleato(2, n // 2)
    j = num_aleato(0, n - h - 1)
    fin = j + h

    C, D = parcial_emparejado(A, B, j, fin)

    C = ascenso_mas_empinado(C, M) # Use the global M here
    D = ascenso_mas_empinado(D, M) # Use the global M here

    return C, D

# Ejecutar algoritmo genético
mejor_ruta = algorit_genet(
    n_poblacion=n_poblacion,
    c_max_ite=c_max_ite,
    seleccionar_inicial=seleccionar_inicial,
    REC_operac_cruce=tsp,
    C_costos=costo
)

print(f"\nMejor ruta encontrada: {mejor_ruta}")
print(f"Costo: {costo(mejor_ruta)}")

import random

# Configuración inicial
random.seed(42)

# Parámetros
n_poblacion = 20
c_max_ite = 100
n_ciudades = 20

# Matriz de costos (ejemplo)
M = [[0]*n_ciudades for _ in range(n_ciudades)]
for i in range(n_ciudades):
    for j in range(i+1, n_ciudades):
        costo = random.randint(10, 99)
        M[i][j] = costo
        M[j][i] = costo

# Función para generar población inicial
def seleccionar_inicial(tam):
    poblacion = []
    for _ in range(tam):
        ruta = list(range(n_ciudades))
        random.shuffle(ruta)
        # Aplicar mejora inicial (opcional)
        # ruta = ascenso_mas_empinado(ruta, M)
        poblacion.append(ruta)
    return poblacion

# Función de costo
def costo(ruta):
    total = 0
    for i in range(len(ruta)-1):
        total += M[ruta[i]][ruta[i+1]]
    total += M[ruta[-1]][ruta[0]]
    return total

# --- Helper functions for tsp (from cell gZusWbo2w7JT) ---
def num_aleato(a, b):
    return random.randint(a, b)

def parcial_emparejado(A, B, inicio, fin):
    n = len(A)
    C = [None] * n
    D = [None] * n

    # Copiar segmentos
    for i in range(inicio, fin + 1):
        C[i] = A[i]
        D[i] = B[i]

    def rellenar(hijo, padre_actual, segmento_copiado, otro_segmento):
        for i in range(n):
            if hijo[i] is None:
                val = padre_actual[i]
                # Si el valor ya está en el hijo, seguimos el mapeo
                while val in hijo:
                    # Buscamos el valor en el segmento que ya copiamos
                    idx = segmento_copiado.index(val)
                    val = otro_segmento[idx]
                hijo[i] = val

    # Para C: usamos valores de B, pero mapeamos contra el segmento de A
    rellenar(C, B, A, B)
    # Para D: usamos valores de A, pero mapeamos contra el segmento de B
    rellenar(D, A, B, A)

    return C, D

def G(X, i, j, M_arg):
    n = len(X)
    a, b = X[i], X[(i + 1) % n]
    c, d = X[j], X[(j + 1) % n]
    # Ganancia = Distancia actual - Distancia nueva
    return (M_arg[a][b] + M_arg[c][d]) - (M_arg[a][c] + M_arg[b][d])

def aplicar_2opt(X, i, j):
    # Invierte el segmento entre i+1 y j
    return X[:i+1] + X[i+1:j+1][::-1] + X[j+1:]

def ascenso_mas_empinado(X, M_arg):
    n = len(X)
    hecho = False
    while not hecho:
        hecho = True
        g_mejor = 0
        movimiento = None

        for i in range(n - 1):
            for j in range(i + 2, n):
                if i == 0 and j == n - 1: continue

                ganancia = G(X, i, j, M_arg)
                if ganancia > g_mejor:
                    g_mejor = ganancia
                    movimiento = (i, j)

        if g_mejor > 0:
            X = aplicar_2opt(X, movimiento[0], movimiento[1])
            hecho = False
    return X
# --- End of Helper functions ---


# Tu función de cruce (tsp) - FULL IMPLEMENTATION
def tsp(A, B):
    # M is globally accessible in this cell
    n = len(A)
    # h es la longitud del segmento, j es el inicio
    h = num_aleato(2, n // 2)
    j = num_aleato(0, n - h - 1)
    fin = j + h

    C, D = parcial_emparejado(A, B, j, fin)

    C = ascenso_mas_empinado(C, M) # Use the global M here
    D = ascenso_mas_empinado(D, M) # Use the global M here

    return C, D

# Ejecutar algoritmo genético
mejor_ruta = algorit_genet(
    n_poblacion=n_poblacion,
    c_max_ite=c_max_ite,
    seleccionar_inicial=seleccionar_inicial,
    REC_operac_cruce=tsp,
    C_costos=costo
)

print(f"\nMejor ruta encontrada: {mejor_ruta}")
print(f"Costo: {costo(mejor_ruta)}")

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
