# Heurísticos

## Problemas de Optimización Combinatoria

Paquete en Python que implementa algoritmos heurísticos y exactos para resolver problemas clásicos de optimización combinatoria.

---

## Descripción

Este proyecto desarrolla una biblioteca en Python orientada a la resolución de problemas clásicos de optimización combinatoria mediante distintos enfoques algorítmicos.

El objetivo principal es comparar algoritmos exactos y heurísticos, analizando:

- Eficiencia computacional
- Complejidad algorítmica
- Calidad de las soluciones obtenidas
- Rendimiento en distintas instancias

Actualmente el proyecto incluye implementaciones para:

- Problema de la Mochila 0/1
- Problema del Agente Viajero (TSP)

---

# Problema de la Mochila 0/1

El problema de la mochila consiste en seleccionar objetos con un peso y un valor asociados para maximizar el beneficio total sin exceder una capacidad límite.

Se denomina **0/1** porque cada objeto únicamente puede:

- No seleccionarse (`0`)
- Seleccionarse completamente (`1`)

No es posible seleccionar fracciones de objetos.

---

## Módulo Mochila 0/1

Implementación de algoritmos heurísticos y exactos:

- Greedy
- Backtracking
- Recocido Simulado

---

# Problema del Agente Viajero (TSP)

El Problema del Agente Viajero (*Traveling Salesman Problem*) consiste en encontrar la ruta más corta posible que permita visitar un conjunto de ciudades exactamente una vez y regresar al punto de origen.

El objetivo es minimizar la distancia total recorrida o el costo total del recorrido.

---

## Módulo Agente Viajero

Implementación de algoritmos y operadores heurísticos:

- Cruce Parcialmente Emparejado (PMX)
- Búsqueda Local 2-OPT
- Algoritmo Genético para TSP

---

# Instalación

## Clonar el repositorio

```bash
git clone https://github.com/me400582-arch/heuristicos
```

## Entrar al proyecto

```bash
cd heuristicos
```

## Instalar el paquete

```bash
pip install .
```

---

# Estructura del Proyecto

```bash
heuristicos/
│
├── heuristicos_pkg/
│   ├── __init__.py
│   ├── knapsack.py
│   └── viajero.py
│
├── tests/
│   ├── test_knapsack.py
│   └── test_viajero.py
│
├── README.md
├── pyproject.toml
├── index.html
└── .gitignore
```

---

# Algoritmos Implementados

## Greedy

Selecciona objetos utilizando la mejor relación valor/peso.

### Características

- Algoritmo heurístico
- Complejidad aproximada `O(n log n)`
- Ejecución rápida
- No garantiza solución óptima

---

## Backtracking

Explora todas las combinaciones posibles de objetos.

### Características

- Algoritmo exacto
- Garantiza la solución óptima
- Complejidad exponencial `O(2^n)`

---

## Recocido Simulado

Metaheurística inspirada en el proceso físico de enfriamiento de metales.

### Características

- Permite escapar de óptimos locales
- Usa aceptación probabilística
- Produce soluciones aproximadas eficientes
- Adecuado para problemas complejos

---

## Cruce Parcialmente Emparejado (PMX)

Operador genético utilizado en problemas de permutaciones como el TSP.

### Características

- Preserva la validez de las permutaciones
- Mantiene relaciones relativas entre ciudades
- Garantiza una biyección completa
- Complejidad aproximada `O(n²)`

---

## Búsqueda Local 2-OPT

Heurística de optimización local que mejora rutas eliminando cruces innecesarios.

### Características

- Técnica de búsqueda local
- Mejora progresivamente las rutas
- Complejidad temporal aproximada entre `O(n²)` y `O(n³)`
- Puede ser costoso para instancias grandes

---

## Algoritmo Genético para TSP

Algoritmo evolutivo inspirado en los principios de selección natural.

### Características

- Usa operadores de cruce y mutación
- Mantiene diversidad poblacional
- Ayuda a evitar óptimos locales
- Genera soluciones aproximadas eficientes
- Adecuado para problemas de gran tamaño

---

# Ejemplo de Uso

## Mochila 0/1 con Greedy

```python
from heuristicos_pkg.knapsack import mochila_greedy

valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidad = 50

seleccion, valor = mochila_greedy(
    valores,
    pesos,
    capacidad
)

print("Objetos seleccionados:", seleccion)
print("Valor total:", valor)
```

---

## Mochila 0/1 con Recocido Simulado

```python
from heuristicos_pkg.knapsack import mochila_recocido_simulado

valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidad = 50

solucion, valor = mochila_recocido_simulado(
    valores,
    pesos,
    capacidad
)

print("Solución:", solucion)
print("Valor obtenido:", valor)
```

---

## Problema del Agente Viajero (TSP)

```python
from heuristicos_pkg.viajero import (
    generar_poblacion,
    calcular_costo
)

M = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

poblacion = generar_poblacion(
    tamano_poblacion=5,
    n=4,
    M=M
)

for ruta in poblacion:
    costo = calcular_costo(ruta, M)

    print("Ruta:", ruta)
    print("Costo:", costo)
```

---

## Otra instancia de ejemplo

```python
valores = [60, 100, 120, 80, 200]
pesos = [10, 20, 30, 15, 40]
capacidad = 70
```

### Nota

Las listas `valores` y `pesos` deben tener la misma longitud.

Ejecutar las pruebas unitarias con:

```bash
pytest
```

Las pruebas verifican:

- Factibilidad de soluciones
- Correctitud de algoritmos exactos
- Consistencia de heurísticas
- Validez de rutas y permutaciones

---

# Tecnologías Utilizadas

- Python
- Pytest
- GitHub
- GitHub Pages
- HTML
- LaTeX

---

# Objetivos Académicos

Este proyecto fue desarrollado con fines educativos para:

- Analizar técnicas heurísticas y exactas
- Comparar complejidad computacional
- Aplicar optimización combinatoria
- Implementar algoritmos metaheurísticos
- Utilizar buenas prácticas de programación

---

# Equipo de Trabajo

- Jose Rodolfo De la Cruz Flores
- Marcela Mendoza Roque
- Carlos Perusi Hernandez Cuellar

---

# Licencia

Proyecto académico desarrollado con fines educativos.
