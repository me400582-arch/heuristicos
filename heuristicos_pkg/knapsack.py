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

    Parámetros
    ----------
    valores : list[int]
        Valores de los objetos.

    pesos : list[int]
        Pesos de los objetos.

    capacidad : int
        Capacidad máxima permitida.

    Retorna
    -------
    tuple
        Objetos seleccionados y valor total.
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
    Resuelve el problema de la mochila
    utilizando backtracking.

    Parámetros
    ----------
    pesos : list[int]
        Pesos de los objetos.

    valores : list[int]
        Valores de los objetos.

    capacidad : int
        Capacidad máxima permitida.

    Retorna
    -------
    tuple
        Mejor valor, peso total y selección binaria.
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

    mejor_valor = 0
    mejor_peso = 0

    mejor_seleccion = [0] * n

    def backtrack(i, peso_actual,
                   valor_actual, seleccion):

        nonlocal mejor_valor
        nonlocal mejor_peso
        nonlocal mejor_seleccion

        if peso_actual > capacidad:
            return

        if i == n:

            if valor_actual > mejor_valor:

                mejor_valor = valor_actual

                mejor_peso = peso_actual

                mejor_seleccion = seleccion[:]

            return

        seleccion[i] = 1

        backtrack(
            i + 1,
            peso_actual + pesos[i],
            valor_actual + valores[i],
            seleccion
        )

        seleccion[i] = 0

        backtrack(
            i + 1,
            peso_actual,
            valor_actual,
            seleccion
        )

    backtrack(0, 0, 0, [0] * n)

    return (
        mejor_valor,
        mejor_peso,
        mejor_seleccion
    )

# RECOCIDO SIMULADO

import random
import math


def mochila_recocido_simulado(
    valores,
    pesos,
    capacidad,
    temperatura=1000,
    enfriamiento=0.95,
    iteraciones=1000
):
    """
    Resuelve el problema de la mochila
    usando recocido simulado.
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

    solucion_actual = [0] * n

    mejor_solucion = solucion_actual[:]

    def evaluar(solucion):

        peso = sum(
            pesos[i]
            for i in range(n)
            if solucion[i]
        )

        valor = sum(
            valores[i]
            for i in range(n)
            if solucion[i]
        )

        if peso > capacidad:
            return 0

        return valor

    valor_actual = evaluar(solucion_actual)

    mejor_valor = valor_actual

    while temperatura > 1:

        for _ in range(iteraciones):

            nueva_solucion = solucion_actual[:]

            i = random.randint(0, n - 1)

            nueva_solucion[i] = 1 - nueva_solucion[i]

            nuevo_valor = evaluar(nueva_solucion)

            diferencia = nuevo_valor - valor_actual

            if (
                diferencia > 0
                or random.random() <
                math.exp(
                    diferencia / temperatura
                )
            ):

                solucion_actual = nueva_solucion

                valor_actual = nuevo_valor

                if valor_actual > mejor_valor:

                    mejor_solucion = solucion_actual[:]

                    mejor_valor = valor_actual

        temperatura *= enfriamiento

    return mejor_solucion, mejor_valor
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
