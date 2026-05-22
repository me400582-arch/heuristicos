"""Algoritmos heurísticos y exactos para el problema de la mochila 0/1."""

import math
import random
from typing import Sequence


def _validar_instancia(
    valores: Sequence[int],
    pesos: Sequence[int],
    capacidad: int,
) -> None:
    if len(valores) != len(pesos):
        raise ValueError("valores y pesos deben tener el mismo tamaño")
    if capacidad < 0:
        raise ValueError("la capacidad no puede ser negativa")
    if any(p <= 0 for p in pesos):
        raise ValueError("todos los pesos deben ser positivos")


def generar_instancia_mochila(
    n_objetos: int = 10,
    valor_min: int = 10,
    valor_max: int = 100,
    peso_min: int = 1,
    peso_max: int = 30,
    capacidad_ratio: float = 0.5,
) -> tuple[list[int], list[int], int]:
    """
    Genera una instancia aleatoria del problema de la mochila.

    La capacidad se calcula como una fracción del peso total para
    que la instancia sea razonable y no trivial.
    """
    if n_objetos <= 0:
        raise ValueError("n_objetos debe ser positivo")
    if valor_min > valor_max:
        raise ValueError("valor_min no puede ser mayor que valor_max")
    if peso_min > peso_max:
        raise ValueError("peso_min no puede ser mayor que peso_max")
    if peso_min <= 0:
        raise ValueError("peso_min debe ser positivo")
    if not (0 < capacidad_ratio <= 1):
        raise ValueError("capacidad_ratio debe estar en el intervalo (0, 1]")

    valores = [random.randint(valor_min, valor_max) for _ in range(n_objetos)]
    pesos = [random.randint(peso_min, peso_max) for _ in range(n_objetos)]
    capacidad = max(1, int(sum(pesos) * capacidad_ratio))
    return valores, pesos, capacidad


def mochila_greedy(
    valores: Sequence[int],
    pesos: Sequence[int],
    capacidad: int,
) -> tuple[list[int], int]:
    """
    Algoritmo greedy para el problema de la mochila.

    Ordena por valor/peso y selecciona mientras haya espacio.
    """
    _validar_instancia(valores, pesos, capacidad)

    indices = list(range(len(valores)))
    indices.sort(key=lambda i: valores[i] / pesos[i], reverse=True)

    total_valor = 0
    peso_actual = 0
    seleccion = []

    for i in indices:
        if peso_actual + pesos[i] <= capacidad:
            seleccion.append(i)
            peso_actual += pesos[i]
            total_valor += valores[i]

    return seleccion, total_valor


def mochila_backtracking(
    pesos: Sequence[int],
    valores: Sequence[int],
    capacidad: int,
) -> tuple[int, int, list[int]]:
    """
    Resuelve la mochila 0/1 usando branch and bound.

    Se ordenan los objetos por valor/peso y se poda con una cota fraccionaria
    para evitar explorar ramas que no pueden mejorar la mejor solución conocida.
    """
    _validar_instancia(valores, pesos, capacidad)

    n = len(pesos)
    if n == 0:
        return 0, 0, []

    items = sorted(
        [(valores[i] / pesos[i], valores[i], pesos[i], i) for i in range(n)],
        reverse=True,
    )

    mejor_valor = 0
    mejor_peso = 0
    mejor_seleccion = [0] * n
    seleccion_actual = [0] * n

    def cota_superior(indice: int, peso_actual: int, valor_actual: int) -> float:
        restante = capacidad - peso_actual
        cota = float(valor_actual)

        j = indice
        while j < n and items[j][2] <= restante:
            _, valor, peso, _ = items[j]
            restante -= peso
            cota += valor
            j += 1

        if j < n and restante > 0:
            _, valor, peso, _ = items[j]
            cota += valor * (restante / peso)

        return cota

    def backtrack(indice: int, peso_actual: int, valor_actual: int) -> None:
        nonlocal mejor_valor, mejor_peso, mejor_seleccion

        if peso_actual > capacidad:
            return

        if cota_superior(indice, peso_actual, valor_actual) <= mejor_valor:
            return

        if indice == n:
            if valor_actual > mejor_valor:
                mejor_valor = valor_actual
                mejor_peso = peso_actual
                mejor_seleccion = seleccion_actual[:]
            return

        _, valor, peso, original_index = items[indice]

        seleccion_actual[original_index] = 1
        backtrack(indice + 1, peso_actual + peso, valor_actual + valor)

        seleccion_actual[original_index] = 0
        backtrack(indice + 1, peso_actual, valor_actual)

    backtrack(0, 0, 0)
    return mejor_valor, mejor_peso, mejor_seleccion


def mochila_recocido_simulado(
    valores: Sequence[int],
    pesos: Sequence[int],
    capacidad: int,
    temperatura: float = 1000.0,
    enfriamiento: float = 0.95,
    iteraciones: int = 1000,
) -> tuple[list[int], int]:
    """
    Resuelve la mochila 0/1 con recocido simulado.

    Devuelve una solución factible y su valor.
    """
    _validar_instancia(valores, pesos, capacidad)

    if temperatura <= 0:
        raise ValueError("temperatura debe ser positiva")
    if not (0 < enfriamiento < 1):
        raise ValueError("enfriamiento debe estar en el intervalo (0, 1)")
    if iteraciones <= 0:
        raise ValueError("iteraciones debe ser positivo")

    n = len(valores)
    if n == 0:
        return [], 0

    solucion_actual = [0] * n

    # Arranque factible aleatorio.
    indices = list(range(n))
    random.shuffle(indices)
    peso_actual = 0
    for i in indices:
        if peso_actual + pesos[i] <= capacidad and random.random() < 0.5:
            solucion_actual[i] = 1
            peso_actual += pesos[i]

    def evaluar(solucion: Sequence[int]) -> tuple[int, int, bool]:
        peso = sum(pesos[i] for i in range(n) if solucion[i])
        valor = sum(valores[i] for i in range(n) if solucion[i])
        return valor, peso, peso <= capacidad

    valor_actual, peso_actual, _ = evaluar(solucion_actual)
    mejor_solucion = solucion_actual[:]
    mejor_valor = valor_actual

    while temperatura > 1:
        for _ in range(iteraciones):
            candidata = solucion_actual[:]
            i = random.randint(0, n - 1)
            candidata[i] = 1 - candidata[i]

            valor_candidata, peso_candidata, es_factible = evaluar(candidata)

            valor_efectivo_actual = (
                valor_actual
                if peso_actual <= capacidad
                else valor_actual - (peso_actual - capacidad) * 10
            )
            valor_efectivo_candidata = (
                valor_candidata
                if es_factible
                else valor_candidata - (peso_candidata - capacidad) * 10
            )

            diferencia = valor_efectivo_candidata - valor_efectivo_actual

            if diferencia > 0 or random.random() < math.exp(diferencia / temperatura):
                solucion_actual = candidata
                valor_actual = valor_candidata
                peso_actual = peso_candidata

                if es_factible and valor_candidata > mejor_valor:
                    mejor_solucion = candidata[:]
                    mejor_valor = valor_candidata

        temperatura *= enfriamiento

    return mejor_solucion, mejor_valor


if __name__ == "__main__":
    valores, pesos, capacidad = generar_instancia_mochila(n_objetos=8)

    print("Valores:", valores)
    print("Pesos:", pesos)
    print("Capacidad:", capacidad)

    seleccion, valor = mochila_greedy(valores, pesos, capacidad)
    print("\n=== GREEDY ===")
    print("Selección:", seleccion)
    print("Valor:", valor)

    mejor_valor, mejor_peso, mejor_seleccion = mochila_backtracking(pesos, valores, capacidad)
    print("\n=== BACKTRACKING ===")
    print("Valor óptimo:", mejor_valor)
    print("Peso:", mejor_peso)
    print("Selección binaria:", mejor_seleccion)

    solucion_rs, valor_rs = mochila_recocido_simulado(valores, pesos, capacidad)
    print("\n=== RECOCIDO SIMULADO ===")
    print("Solución:", solucion_rs)
    print("Valor:", valor_rs)
