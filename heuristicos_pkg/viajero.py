import random
from dataclasses import dataclass


def generar_matriz_aleatoria(
    n,
    simetrica=True,
    minimo=1,
    maximo=100
):
    return TSP.generar_matriz_aleatoria(
        n,
        simetrica=simetrica,
        minimo=minimo,
        maximo=maximo
    )


def generar_poblacion(
    tamano_poblacion,
    n
):

    if tamano_poblacion <= 0:
        raise ValueError(
            "tamano_poblacion debe ser positivo"
        )

    if n <= 0:
        raise ValueError(
            "n debe ser positivo"
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


def calcular_costo(
    ruta,
    matriz_costos
):

    return TSP(
        matriz_costos
    ).calcular_costo(
        ruta
    )


def dos_opt(
    ruta,
    matriz_costos
):

    return TSP(
        matriz_costos
    ).dos_opt(
        ruta
    )


@dataclass
class TSP:

    matriz_costos:list

    def __post_init__(self):

        n=len(
            self.matriz_costos
        )

        if n==0:

            raise ValueError(
                "La matriz no puede estar vacía"
            )

        for fila in self.matriz_costos:

            if len(fila)!=n:

                raise ValueError(
                    "La matriz debe ser cuadrada"
                )


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

            for j in range(i+1,n):

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


    def generar_ruta(self):

        n=len(
            self.matriz_costos
        )

        ruta=list(
            range(n)
        )

        random.shuffle(
            ruta
        )

        return ruta


    def generar_poblacion(
        self,
        tamano_poblacion
    ):

        n=len(
            self.matriz_costos
        )

        return [

            self.generar_ruta()

            for _ in range(
                tamano_poblacion
            )
        ]


    def calcular_costo(
        self,
        ruta
    ):

        n=len(
            ruta
        )

        costo=0

        for i in range(
            n-1
        ):

            costo+=self.matriz_costos[
                ruta[i]
            ][
                ruta[i+1]
            ]

        costo+=self.matriz_costos[
            ruta[-1]
        ][
            ruta[0]
        ]

        return costo


    def dos_opt(
        self,
        ruta
    ):

        mejor=ruta.copy()

        mejor_costo=self.calcular_costo(
            mejor
        )

        mejora=True

        while mejora:

            mejora=False

            for i in range(
                1,
                len(mejor)-1
            ):

                for j in range(
                    i+1,
                    len(mejor)
                ):

                    nueva=(
                        mejor[:i]
                        +
                        mejor[i:j][::-1]
                        +
                        mejor[j:]
                    )

                    costo=self.calcular_costo(
                        nueva
                    )

                    if costo<mejor_costo:

                        mejor=nueva

                        mejor_costo=costo

                        mejora=True

        return mejor
