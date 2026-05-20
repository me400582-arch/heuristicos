import random

class TSP:
    def __init__(self, matriz_costos):
        """Inicializa el problema con la matriz de distancias"""
        self.M = matriz_costos

    def generar_ruta(self, n):
        """Genera una permutación válida de ciudades"""
        ruta = list(range(n))
        random.shuffle(ruta)
        return ruta

    def generar_poblacion(self, tamano_poblacion, n):
        """Genera una población de rutas válidas"""
        poblacion = []
        for _ in range(tamano_poblacion):
            ruta = self.generar_ruta(n)
            poblacion.append(ruta)
        return poblacion

    def calcular_costo(self, ruta):
        """Calcula el costo total de una ruta (ciclo cerrado)"""
        costo = 0
        n = len(ruta)

        for i in range(n):
            origen = ruta[i]
            destino = ruta[(i + 1) % n]  # regresa al inicio
            costo += self.M[origen][destino]

        return costo

    def dos_opt(self, ruta):
        """Mejora una ruta usando 2-OPT"""
        mejor = ruta[:]
        mejor_costo = self.calcular_costo(mejor)

        mejora = True
        while mejora:
            mejora = False

            for i in range(1, len(ruta) - 1):
                for j in range(i + 1, len(ruta)):
                    nueva_ruta = mejor[:]
                    nueva_ruta[i:j] = reversed(nueva_ruta[i:j])

                    nuevo_costo = self.calcular_costo(nueva_ruta)

                    if nuevo_costo < mejor_costo:
                        mejor = nueva_ruta
                        mejor_costo = nuevo_costo
                        mejora = True

            ruta = mejor

        return mejor, mejor_costo
