import math

def distancia(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def vecino_mas_cercano(ciudades):
    n = len(ciudades)
    visitado = [False] * n
    ruta = [0]
    visitado[0] = True

    for _ in range(n - 1):
        ultimo = ruta[-1]
        mejor = None
        mejor_dist = float('inf')

        for i in range(n):
            if not visitado[i]:
                d = distancia(ciudades[ultimo], ciudades[i])
                if d < mejor_dist:
                    mejor_dist = d
                    mejor = i

        ruta.append(mejor)
        visitado[mejor] = True

    return ruta
