from dataclasses import dataclass
import random


@dataclass
class TSP:
    """
    Clase para representar el problema
    del agente viajero.
    """

    matriz_costos: list[list[int]]

    def __post_init__(self):

        if not self.matriz_costos:
            raise ValueError(
                "la matriz no puede estar vacía"
            )

        n = len(self.matriz_costos)

        for fila in self.matriz_costos:

            if len(fila) != n:

                raise ValueError(
                    "la matriz debe ser cuadrada"
                )

    def generar_ruta(self, n):

        ruta = list(range(n))

        random.shuffle(ruta)

        return ruta

    def calcular_costo(self, ruta):

        costo = 0

        n = len(ruta)

        for i in range(n):

            origen = ruta[i]

            destino = ruta[(i + 1) % n]

            costo += self.matriz_costos[
                origen
            ][destino]

        return costo

    def dos_opt(self, ruta):

        mejor_ruta = ruta[:]

        mejor_costo = self.calcular_costo(
            mejor_ruta
        )

        mejora = True

        while mejora:

            mejora = False

            n = len(mejor_ruta)

            for i in range(1, n - 1):

                for j in range(i + 1, n):

                    nueva_ruta = (
                        mejor_ruta[:i]
                        + mejor_ruta[i:j][::-1]
                        + mejor_ruta[j:]
                    )

                    nuevo_costo = (
                        self.calcular_costo(
                            nueva_ruta
                        )
                    )

                    if nuevo_costo < mejor_costo:

                        mejor_ruta = nueva_ruta

                        mejor_costo = nuevo_costo

                        mejora = True

        return mejor_ruta, mejor_costo
