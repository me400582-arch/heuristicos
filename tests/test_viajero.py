from heuristicos_pkg.tsp import vecino_mas_cercano

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
  "Es un algoritmo genético clásico con mejora implícita en REC"

def algorit_genet(n_poblacion, c_max_ite, seleccionar_inicial, REC_operac_cruce, C_costos):
    c = 1 # contador de generadores
    P = seleccionar_inicial(n_poblacion) # genera la poblacion inicial con el tamaño

    P.sort(key = C_costos) # Ordenar por costo (menor es mejor)
    # .sort ordena la lista y key ordela la lista a base de los costos

    X_mejor = P[0] # Guarda la mejor solución actual
    MejorCosto = C_costos(P[0]) # Guarda el mejor costo

    while c <= c_max_ite: # El contador de generadores es menor que el max de itera
        nuevos = [] # lista donde guarda los hijos
        for i in range(n_poblacion // 2): # ciclo i del tamaño de pobla entre 2, cada una genera 2 itercaciones
            padre1 = P[2 * i] # empiezas desde el 0, generes una iteracion
            padre2 = P[2 * i + 1] # quedara como una coordenada

            hijo1, hijo2 = REC_operac_cruce(padre1, padre2) # Recibe padre y devuelve hijos

            nuevos.append(hijo1) #guardas el hijo 1 o 2
            nuevos.append(hijo2) # .append agrega una elemento a la lista

        # Unir población actual + nueva
        P = P + nuevos # se combina la población actual con los hijos

        # Ordenar toda la población
        P.sort(key=C_costos) # Ordena la poblaciones de viejos + nuevos

        # Mantener solo los mejores (elitismo)
        P = P[:n_poblacion] # Elimina soluciones malas

        # Actualizar mejor solución
        CurCosto = C_costos(P[0]) # Toma el costo del individuo actual
        if CurCosto < MejorCosto: # Si es mejor costos
            X_mejor = P[0] # Actualizas el mejor solución
            MejorCosto = CurCosto # Actualiza el mejor costo

        c += 1 # Se aumenta el contador

    return X_mejor
  def algorit_genet(n_poblacion, c_max_ite, seleccionar_inicial, REC_operac_cruce, C_costos, prob_cruce=0.9, prob_mutacion=0.1):
    """
    Algoritmo genético completo

    Parámetros adicionales:
    - prob_cruce: probabilidad de cruce (0.7-0.9 típico)
    - prob_mutacion: probabilidad de mutación después del cruce (0.01-0.1 típico)
    """
    c = 1
    P = seleccionar_inicial(n_poblacion)

    # Ordenar por costo (menor es mejor)
    P.sort(key=C_costos)

    X_mejor = P[0][:]
    MejorCosto = C_costos(P[0])

    # Estadísticas (opcional)
    print(f"Gen 0: Mejor costo = {MejorCosto}")

    while c <= c_max_ite:
        nuevos = []

        # Selección por torneo (mejor que solo tomar los primeros)
        def seleccionar_padre(poblacion):
            # Torneo de tamaño 2
            i1 = random.randint(0, len(poblacion) - 1)
            i2 = random.randint(0, len(poblacion) - 1)
            return poblacion[i1] if C_costos(poblacion[i1]) < C_costos(poblacion[i2]) else poblacion[i2]

        while len(nuevos) < n_poblacion:
            padre1 = seleccionar_padre(P)
            padre2 = seleccionar_padre(P)

            # Cruce con probabilidad prob_cruce
            if random.random() < prob_cruce:
                hijo1, hijo2 = REC_operac_cruce(padre1[:], padre2[:])
            else:
                hijo1, hijo2 = padre1[:], padre2[:]

            # Mutación simple (intercambiar dos posiciones)
            if random.random() < prob_mutacion:
                i, j = random.sample(range(len(hijo1)), 2)
                hijo1[i], hijo1[j] = hijo1[j], hijo1[i]

            if random.random() < prob_mutacion:
                i, j = random.sample(range(len(hijo2)), 2)
                hijo2[i], hijo2[j] = hijo2[j], hijo2[i]

            nuevos.append(hijo1)
            nuevos.append(hijo2)

        # Unir y seleccionar los mejores
        P = P + nuevos[:n_poblacion]
        P.sort(key=C_costos)
        P = P[:n_poblacion]

        # Actualizar mejor solución
        CurCosto = C_costos(P[0])
        if CurCosto < MejorCosto:
            X_mejor = P[0][:]
            MejorCosto = CurCosto

        # Mostrar progreso cada 100 generaciones
        if c % 100 == 0:
            print(f"Gen {c}: Mejor costo = {MejorCosto}")

        c += 1

    return X_mejor
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

def alet_numero(a, b): # Se busca un numero aletorio de entre a y b
    return random.randint(a, b) #( usando .randint)
"El numero r a una permuuacion es decir (desenrutado lexicográfico) "

def perm_desen_lexi(r, n): # Tomando un r a una permutución n
    elementos = list(range(n)) # se crea una lista de 0 hasta n-1
    perm = [] # Una lista vacia llamada perm, la vamos a construir

    for i in range(n, 0, -1): # va de n hasta 1 hacia atras
        f = math.factorial(i - 1) # son las permutuaciones de (i-1)!
        idx = r // f # división entera
        r = r % f # solo importa el residuo, permite hacer la permutacion

        perm.append(elementos.pop(idx))
        # .pop elimina y devuelve el elemento idx y lo agraga a la permutacion
    return perm

" Ascenso empinado 2-opt"
def ascenso_m_empinado(X):
    # Aquí puedes poner tu implementación real
    return X  # placeholder


# Algoritmo principal
def generar_poblacion(tamano_poblacion, n):
    P = []

    for i in range(tamano_poblacion):
        r = alet_numero(0, math.factorial(n) - 1)

        P_i = perm_desen_lexi(r, n)

        P_i = ascenso_m_empinado(P_i)

        P.append(P_i)

    return P
