# Heurísticos: Mochila 0/1 y Agente Viajero

## Descripción general

Este proyecto proporciona una biblioteca en Python que implementa
algoritmos exactos y heurísticos para **dos** problemas clásicos de
optimización combinatoria:

- **Mochila 0/1** (0/1 knapsack) – se seleccionan elementos con peso y
  valor para maximizar el beneficio sin superar una capacidad fija.
- **Problema del agente viajero** (TSP) – se busca la ruta más corta
  que visita todas las ciudades una sola vez y vuelve al punto de
  partida.

El objetivo es comparar la eficiencia, complejidad y calidad de
las soluciones de cada algoritmo. La rúbrica del proyecto exige
que la documentación sea clara, con instrucciones de instalación y
ejemplos de uso.

## Algoritmos implementados

La biblioteca incluye los siguientes métodos:

| Problema | Algoritmo | Descripción |
|---------|-----------|-------------|
| Mochila 0/1 | **Greedy** | Selecciona elementos ordenados por relación valor/peso hasta completar la capacidad. |
| Mochila 0/1 | **Backtracking (Branch and Bound)** | Explora combinaciones posibles con poda basada en una cota superior para garantizar la mejor solución posible. |
| Mochila 0/1 | **Recocido Simulado** | Metaheurística que explora soluciones vecinas aceptando empeoramientos probabilísticos para evitar óptimos locales. |
| Agente Viajero | **Generación aleatoria de matrices y rutas** | Crea matrices de costos simétricas o asimétricas y genera rutas/poblaciones iniciales aleatorias. |
| Agente Viajero | **Cálculo de costo** | Evalúa el costo total de recorrer una ruta cerrando el ciclo (vuelta a la ciudad inicial). |
| Agente Viajero | **Búsqueda local 2‑OPT** | Intercambia segmentos de una ruta para eliminar cruces y reducir la distancia total. |

Además, el módulo de la mochila define dos clases con
`@dataclass`:

- `InstanciaMochila`: encapsula las listas de valores, pesos y la
  capacidad de la mochila.
- `SolucionMochila`: almacena la selección (vector binario o índices),
  el valor total y el peso total de una solución.

Estas clases facilitan el manejo de datos y cumplen con la indicación
del profesor de utilizar dataclasses para estructurar las
instancias.

## Estructura del proyecto

heuristicos-main/
├── heuristicos_pkg/
│   ├── __init__.py              # Permite importar el paquete como módulo
│   ├── knapsack.py              # Implementa los algoritmos de la mochila
│   └── viajero.py               # Implementa los algoritmos del TSP
│
├── tests/
│   ├── test_knapsack.py         # Pruebas unitarias para la mochila
│   └── test_viajero.py          # Pruebas unitarias para el TSP
│
├── Ejemplos_uso_Heuristicos (2).ipynb  # Notebook con ejemplos de uso
├── index.html                   # Página web de presentación del proyecto
├── pyproject.toml               # Archivo de configuración del paquete
└── README.md                    # Este documento

## Instalación local

Para instalar la biblioteca en tu equipo o entorno virtual de
Python, sigue estos pasos en la terminal. Cada línea está
comentada para aclarar su función:

```bash
# Descarga el repositorio desde GitHub (solo la primera vez)
git clone https://github.com/me400582-arch/heuristicos.git

# Entra en el directorio del proyecto recién clonado
cd heuristicos

# Instala el paquete en el entorno actual de Python (puede requerir privilegios de escritura)
pip install .

# Ejecuta las pruebas unitarias para comprobar que todo funciona correctamente
pytest

# Clonamos el repositorio en la sesión de Colab.
!git clone https://github.com/me400582-arch/heuristicos.git

# Entramos en la carpeta del repositorio para trabajar con el código.
%cd heuristicos

# Instalamos el paquete localmente en el entorno de Colab.
!pip install .

# Importamos todas las funciones necesarias del módulo de la mochila.
from heuristicos_pkg.knapsack import (
    generar_instancia_mochila,
    mochila_greedy,
    mochila_recocido_simulado,
    mochila_backtracking,
)

# Generamos una instancia de la mochila con 50 objetos (valores y pesos aleatorios).
valores, pesos, capacidad = generar_instancia_mochila(n_objetos=50)

# Mostramos las listas de valores, pesos y la capacidad generada.
print("Valores:", valores)
print("Pesos:", pesos)
print("Capacidad:", capacidad)

# Resolución con el algoritmo greedy: devuelve la selección y el valor total.
seleccion, valor = mochila_greedy(valores, pesos, capacidad)
print("Selección (greedy):", seleccion)
print("Valor total (greedy):", valor)

# Resolución con recocido simulado: encuentra una solución aproximada.
seleccion, valor = mochila_recocido_simulado(valores, pesos, capacidad)
print("Selección (recocido):", seleccion)
print("Valor total (recocido):", valor)

# Resolución exacta con backtracking (branch and bound).
valor_optimo, peso_optimo, seleccion_optima = mochila_backtracking(pesos, valores, capacidad)
print("Valor óptimo (backtracking):", valor_optimo)
print("Peso óptimo:", peso_optimo)
print("Selección óptima:", seleccion_optima)

# Importamos las funciones y la clase del TSP.
from heuristicos_pkg.viajero import generar_matriz_aleatoria, TSP

# Generamos una matriz de costos simétrica para 20 ciudades.
matriz = generar_matriz_aleatoria(20, simetrica=True)
print("Matriz generada:", matriz)

# Creamos una instancia del problema con esa matriz.
tsp = TSP(matriz)

# Generamos una ruta inicial aleatoria.
ruta = tsp.generar_ruta()
print("Ruta inicial:", ruta)

# Calculamos el costo de la ruta inicial.
costo = tsp.calcular_costo(ruta)
print("Costo inicial:", costo)

# Mejora de la ruta mediante la heurística 2‑OPT.
mejor_ruta, mejor_costo = tsp.dos_opt(ruta)
print("Ruta mejorada:", mejor_ruta)
print("Costo mejorado:", mejor_costo)

# Finalmente, ejecutamos las pruebas unitarias para asegurarnos de que todo funciona.
!pytest
