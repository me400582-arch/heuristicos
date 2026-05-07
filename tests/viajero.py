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