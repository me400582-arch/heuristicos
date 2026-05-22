import random
import math

# GENERADOR DE INSTANCIAS ALEATORIAS

def generar_instancia_mochila(n_objetos=10,
                               valor_min=10,
                               valor_max=100,
                               peso_min=1,
                               peso_max=30,
                               capacidad_ratio=0.5):
    """
    Genera una instancia aleatoria del problema de la mochila.

    Parámetros:
    - n_objetos: cantidad de objetos
    - valor_min, valor_max: rango de valores
    - peso_min, peso_max: rango de pesos
    - capacidad_ratio:
        porcentaje del peso total usado como capacidad

    Retorna:
    - valores
    - pesos
    - capacidad
    """

    valores = [random.randint(valor_min, valor_max)
               for _ in range(n_objetos)]

    pesos = [random.randint(peso_min, peso_max)
             for _ in range(n_objetos)]

    capacidad = int(sum(pesos) * capacidad_ratio)

    return valores, pesos, capacidad

# ALGORITMO GREEDY

def mochila_greedy(valores, pesos, capacidad):
    """
    Algoritmo greedy para el problema de la mochila.
    Ordena por valor/peso y selecciona mientras haya espacio.
    """
    if len(valores) != len(pesos):
        raise ValueError(
            "valores y pesos deben tener el mismo tamaño"
        )

    if capacidad < 0:
        raise ValueError(
            "la capacidad no puede ser negativa"
        )

    if any(p <= 0 for p in pesos):
        raise ValueError(
            "todos los pesos deben ser positivos"
        )
    n = len(valores)

    indices = list(range(n))

    indices.sort(
        key=lambda i: valores[i] / pesos[i],
        reverse=True
    )

    total_valor = 0
    peso_actual = 0
    seleccion = []

    for i in indices:

        if peso_actual + pesos[i] <= capacidad:

            seleccion.append(i)

            peso_actual += pesos[i]

            total_valor += valores[i]

    return seleccion, total_valor

# BACKTRACKING

def mochila_backtracking(pesos, valores, capacidad):
    """
    Solución óptima usando backtracking.
    """
      if len(valores) != len(pesos):
        raise ValueError(
            "valores y pesos deben tener el mismo tamaño"
        )

    if capacidad < 0:
        raise ValueError(
            "la capacidad no puede ser negativa"
        )

    if any(p <= 0 for p in pesos):
        raise ValueError(
            "todos los pesos deben ser positivos"
        )

    n = len(pesos)

    best = [0, 0, []]

    def bt(idx, current):

        if idx == n:

            peso = sum(
                pesos[i] * current[i]
                for i in range(n)
            )

            valor = sum(
                valores[i] * current[i]
                for i in range(n)
            )

            if peso <= capacidad and valor > best[0]:

                best[0] = valor
                best[1] = peso
                best[2] = current[:]

            return

        # elegir objeto
        current.append(1)

        bt(idx + 1, current)

        current.pop()

        # no elegir objeto
        current.append(0)

        bt(idx + 1, current)

        current.pop()

    bt(0, [])

    return best

# RECOCIDO SIMULADO

def mochila_recocido_simulado(valores,
                               pesos,
                               capacidad,
                               T0=1000,
                               alpha=0.999,
                               iteraciones=5000):
    """
    Algoritmo de recocido simulado
    para el problema de la mochila.
    """
    if len(valores) != len(pesos):
        raise ValueError(
            "valores y pesos deben tener el mismo tamaño"
        )

    if capacidad < 0:
        raise ValueError(
            "la capacidad no puede ser negativa"
        )

    if any(p <= 0 for p in pesos):
        raise ValueError(
            "todos los pesos deben ser positivos"
        )
    n = len(valores)

    # solución inicial
    X = [0] * n

    peso_actual = 0
    valor_actual = 0

    mejor_X = X[:]
    mejor_valor = 0

    T = T0

    for _ in range(iteraciones):

        # índice aleatorio
        j = random.randint(0, n - 1)

        Y = X[:]

        # cambiar bit
        Y[j] = 1 - Y[j]

        nuevo_peso = peso_actual
        nuevo_valor = valor_actual

        # agregar objeto
        if Y[j] == 1:

            nuevo_peso += pesos[j]

            nuevo_valor += valores[j]

        # quitar objeto
        else:

            nuevo_peso -= pesos[j]

            nuevo_valor -= valores[j]

        # verificar factibilidad
        if nuevo_peso <= capacidad:

            delta = nuevo_valor - valor_actual

            # mejora
            if delta > 0:

                X = Y

                peso_actual = nuevo_peso

                valor_actual = nuevo_valor

            # aceptar peor solución
            else:

                prob = math.exp(delta / T)

                if random.random() < prob:

                    X = Y

                    peso_actual = nuevo_peso

                    valor_actual = nuevo_valor

            # actualizar mejor solución
            if valor_actual > mejor_valor:

                mejor_valor = valor_actual

                mejor_X = X[:]

        # enfriamiento
        T *= alpha

    return mejor_X, mejor_valor

# EJEMPLO DE USO

if __name__ == "__main__":

    valores, pesos, capacidad = generar_instancia_mochila(
        n_objetos=8
    )

    print("Valores:", valores)
    print("Pesos:", pesos)
    print("Capacidad:", capacidad)

    print("\n=== GREEDY ===")

    seleccion, valor = mochila_greedy(
        valores,
        pesos,
        capacidad
    )

    print("Selección:", seleccion)
    print("Valor:", valor)

    print("\n=== BACKTRACKING ===")

    mejor = mochila_backtracking(
        pesos,
        valores,
        capacidad
    )

    print("Valor óptimo:", mejor[0])
    print("Peso:", mejor[1])
    print("Selección binaria:", mejor[2])

    print("\n=== RECOCIDO SIMULADO ===")

    solucion_rs, valor_rs = mochila_recocido_simulado(
        valores,
        pesos,
        capacidad
    )

    print("Solución:", solucion_rs)
    print("Valor:", valor_rs)
