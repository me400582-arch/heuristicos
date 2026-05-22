from dataclasses import dataclass
import random
def generar_matriz_aleatoria(n, simetrica=True, minimo=1, maximo=100):
    return TSP.generar_matriz_aleatoria(
        n,
        simetrica=simetrica,
        minimo=minimo,
        maximo=maximo,
    )

def generar_poblacion(tamano_poblacion, n):
    return [random.sample(range(n), n) for _ in range(tamano_poblacion)]

def calcular_costo(ruta, matriz_costos):
    return TSP(matriz_costos).calcular_costo(ruta)

def dos_opt(ruta, matriz_costos):
    return TSP(matriz_costos).dos_opt(ruta)

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
@staticmethod
def generar_matriz_aleatoria(
    n,
    simetrica=True,
    minimo=1,
    maximo=100
):

    if n<=0:
        raise ValueError(
            "n debe ser positivo"
        )

    matriz=[[0]*n for _ in range(n)]

    for i in range(n):

        for j in range(
            i+1,
            n
        ):

            costo=random.randint(
                minimo,
                maximo
            )

            matriz[i][j]=costo

            if simetrica:

                matriz[j][i]=costo

            else:

                matriz[j][i]=random.randint(
                    minimo,
                    maximo
                )

    return matriz


def generar_poblacion(
    self,
    tamano_poblacion,
    n=None
):

    if tamano_poblacion<=0:

        raise ValueError(
            "tamano_poblacion debe ser positivo"
        )

    if n is None:

        n=len(
            self.matriz_costos
        )

    return [

        random.sample(
            range(n),
            n
        )

        for _ in range(
            tamano_poblacion
        )
    ]
