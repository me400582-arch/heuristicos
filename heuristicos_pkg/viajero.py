"""Utilidades heurísticas para el problema del agente viajero (TSP)."""

import random
from dataclasses import dataclass
from typing import Sequence


def generar_matriz_aleatoria(
    n: int,
    simetrica: bool = True,
    minimo: int = 1,
    maximo: int = 100,
) -> list[list[int]]:
    """Crea una matriz de costos aleatoria para un TSP de tamaño n."""
    return TSP.generar_matriz_aleatoria(
        n,
        simetrica=simetrica,
        minimo=minimo,
        maximo=maximo,
    )


def generar_poblacion(
    tamano_poblacion: int,
    n: int,
) -> list[list[int]]:
    """Genera una población aleatoria de rutas."""
    if tamano_poblacion <= 0:
        raise ValueError("tamano_poblacion debe ser positivo")
    if n <= 0:
        raise ValueError("n debe ser positivo")

    return [random.sample(range(n), n) for _ in range(tamano_poblacion)]


def calcular_costo(
    ruta: Sequence[int],
    matriz_costos: Sequence[Sequence[int]],
) -> int:
    """Calcula el costo total de una ruta."""
    return TSP(matriz_costos).calcular_costo(ruta)


def dos_opt(
    ruta: Sequence[int],
    matriz_costos: Sequence[Sequence[int]],
) -> tuple[list[int], int]:
    """Optimiza una ruta con 2‑OPT y devuelve ruta y costo."""
    return TSP(matriz_costos).dos_opt(ruta)


@dataclass
class TSP:
    """Representa una instancia del problema del agente viajero."""

    matriz_costos: list[list[int]]

    def __post_init__(self) -> None:
        n = len(self.matriz_costos)
        if n == 0:
            raise ValueError("La matriz no puede estar vacía")
        for fila in self.matriz_costos:
            if len(fila) != n:
                raise ValueError("La matriz debe ser cuadrada")

    @staticmethod
    def generar_matriz_aleatoria(
        n: int,
        simetrica: bool = True,
        minimo: int = 1,
        maximo: int = 100,
    ) -> list[list[int]]:
        """Genera una matriz de costos aleatoria."""
        if n <= 0:
            raise ValueError("n debe ser positivo")
        if minimo > maximo:
            raise ValueError("minimo no puede ser mayor que maximo")
        if minimo < 0:
            raise ValueError("minimo no puede ser negativo")

        matriz = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                costo = random.randint(minimo, maximo)
                matriz[i][j] = costo
                matriz[j][i] = costo if simetrica else random.randint(minimo, maximo)

        return matriz

    def generar_ruta(self, n: int | None = None) -> list[int]:
        """Genera una ruta aleatoria como permutación de las ciudades."""
        n_ciudades = len(self.matriz_costos)
        if n is not None and n != n_ciudades:
            raise ValueError("n no coincide con el tamaño de la matriz")
        ruta = list(range(n_ciudades))
        random.shuffle(ruta)
        return ruta

    def generar_poblacion(
        self,
        tamano_poblacion: int,
        n: int | None = None
    ) -> list[list[int]]:
        """Genera una población de rutas aleatorias."""
        if tamano_poblacion <= 0:
            raise ValueError("tamano_poblacion debe ser positivo")
        n_ciudades = len(self.matriz_costos)
        if n is not None and n != n_ciudades:
            raise ValueError("n no coincide con el tamaño de la matriz")
        return [self.generar_ruta() for _ in range(tamano_poblacion)]

    def calcular_costo(self, ruta: Sequence[int]) -> int:
        """Calcula el costo de la ruta cerrada."""
        n = len(self.matriz_costos)
        if len(ruta) != n:
            raise ValueError("La ruta debe contener exactamente una ciudad por nodo")
        if sorted(ruta) != list(range(n)):
            raise ValueError("La ruta debe ser una permutación válida de las ciudades")

        costo = 0
        for i in range(n - 1):
            costo += self.matriz_costos[ruta[i]][ruta[i + 1]]
        # cerrar el ciclo
        costo += self.matriz_costos[ruta[-1]][ruta[0]]
        return costo

    def dos_opt(self, ruta: Sequence[int]) -> tuple[list[int], int]:
        """Aplica 2‑OPT hasta alcanzar un óptimo local."""
        mejor = list(ruta)
        mejor_costo = self.calcular_costo(mejor)

        mejora = True
        while mejora:
            mejora = False
            for i in range(1, len(mejor) - 1):
                for j in range(i + 1, len(mejor)):
                    if j - i == 1:
                        continue
                    nueva = mejor[:i] + mejor[i:j][::-1] + mejor[j:]
                    costo = self.calcular_costo(nueva)
                    if costo < mejor_costo:
                        mejor = nueva
                        mejor_costo = costo
                        mejora = True
        return mejor, mejor_costo
