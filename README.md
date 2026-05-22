# Heurísticos: Mochila 0/1 y Agente Viajero

## Descripción general

Este proyecto implementa una biblioteca en Python orientada a la resolución de problemas clásicos de optimización combinatoria mediante algoritmos exactos y heurísticos.

Los problemas abordados son:

- **Problema de la Mochila 0/1 (Knapsack Problem)**
- **Problema del Agente Viajero (Travelling Salesman Problem - TSP)**

El objetivo principal es comparar diferentes estrategias de solución, analizando:

- Calidad de las soluciones
- Complejidad computacional
- Eficiencia de ejecución
- Diferencias entre algoritmos exactos y heurísticos

La biblioteca fue desarrollada utilizando buenas prácticas de programación en Python:

- Modularización
- Uso de `dataclasses`
- Documentación
- Pruebas unitarias con `pytest`
- Notebook de ejemplos de uso

---

# Problema de la Mochila 0/1

El problema de la mochila consiste en seleccionar objetos con:

- un peso
- un valor o beneficio

de forma que:

- el peso total no exceda la capacidad máxima
- el valor total sea máximo

Este problema pertenece a la clase de problemas NP-Completo y es ampliamente utilizado en:

- logística
- optimización de recursos
- finanzas
- inteligencia artificial

---

# Algoritmos implementados para Mochila

## Greedy

El algoritmo greedy selecciona objetos utilizando la relación:

\[
\frac{valor}{peso}
\]

Los elementos se ordenan de mayor a menor según dicha razón y se agregan mientras exista capacidad disponible.

### Ventajas

- Muy rápido
- Fácil de implementar

### Desventajas

- No garantiza solución óptima

---

## Backtracking con Branch and Bound

Este método explora combinaciones posibles de objetos utilizando poda inteligente.

Se calcula una cota superior para evitar explorar ramas que no pueden mejorar la mejor solución encontrada.

### Características

- Algoritmo exacto
- Garantiza solución óptima
- Mayor costo computacional

---

## Recocido Simulado

Metaheurística inspirada en procesos físicos de enfriamiento de materiales.

Permite aceptar temporalmente soluciones peores con cierta probabilidad para evitar óptimos locales.

### Características

- Aproximación heurística
- Buena exploración del espacio de búsqueda
- No garantiza óptimo global

---

# Problema del Agente Viajero (TSP)

El TSP consiste en encontrar la ruta de menor costo que:

- visite todas las ciudades exactamente una vez
- regrese al punto inicial

Es uno de los problemas más importantes de optimización combinatoria y tiene aplicaciones en:

- rutas de transporte
- logística
- redes
- manufactura
- robótica

---

# Algoritmos implementados para TSP

## Generación de matrices aleatorias

Se implementa la creación de matrices de costos:

- simétricas
- asimétricas

para construir instancias aleatorias del problema.

---

## Generación de rutas y poblaciones

El sistema genera rutas aleatorias válidas utilizando permutaciones de ciudades.

También se generan poblaciones de rutas para posibles algoritmos evolutivos futuros.

---

## Cálculo de costo

Se calcula el costo total de una ruta cerrando el ciclo:

\[
c_{total} = \sum c_{ij}
\]

incluyendo el regreso a la ciudad inicial.

---

## Heurística 2-OPT

El algoritmo 2-OPT mejora rutas intercambiando segmentos para eliminar cruces innecesarios.

### Funcionamiento

- Selecciona dos aristas
- Invierte un segmento de la ruta
- Conserva el cambio si mejora el costo total

### Ventajas

- Reduce considerablemente la distancia
- Implementación relativamente sencilla
- Mejora óptimos locales

---

# Uso de Dataclasses

El módulo de mochila implementa las siguientes clases:

## InstanciaMochila

Representa una instancia del problema:

```python
@dataclass
class InstanciaMochila:
    valores: list[int]
    pesos: list[int]
    capacidad: int
```

---

## SolucionMochila

Representa una solución obtenida:

```python
@dataclass
class SolucionMochila:
    seleccion: list[int]
    valor: int
    peso: int
```

El uso de `dataclass` permite:

- código más limpio
- mejor organización
- facilidad de mantenimiento
- mejor representación de datos

---

# Estructura del proyecto

```text
heuristicos-main/
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
├── ejemplos_heuristicos.ipynb
│
├── pyproject.toml
├── README.md
└── index.html
```

---

# Instalación

## Clonar el repositorio

```bash
! git clone https://github.com/me400582-arch/heuristicos
```

---

## Entrar al proyecto

```bash
%cd heuristicos
```

---

## Instalar el paquete

```bash
! pip install .
```

---

# Ejemplo de uso — Mochila

```python
from heuristicos_pkg.knapsack import (
    generar_instancia_mochila,
    mochila_greedy,
    mochila_backtracking,
    mochila_recocido_simulado,
)

# Generar instancia aleatoria
valores, pesos, capacidad = generar_instancia_mochila(n_objetos=5)

print("Valores:", valores)
print("Pesos:", pesos)
print("Capacidad:", capacidad)

# Greedy
seleccion, valor = mochila_greedy(valores, pesos, capacidad)

print("\n=== GREEDY ===")
print("Selección:", seleccion)
print("Valor:", valor)

# Backtracking
valor_optimo, peso_optimo, seleccion_optima = mochila_backtracking(
    pesos,
    valores,
    capacidad
)

print("\n=== BACKTRACKING ===")
print("Selección:", seleccion_optima)
print("Valor óptimo:", valor_optimo)
print("Peso:", peso_optimo)

# Recocido Simulado
solucion_rs, valor_rs = mochila_recocido_simulado(
    valores,
    pesos,
    capacidad
)

print("\n=== RECOCIDO SIMULADO ===")
print("Solución:", solucion_rs)
print("Valor:", valor_rs)
print("Peso:", peso_optimo)
```

---
# Ejemplo de uso — TSP

```python
from heuristicos_pkg.viajero import (
    generar_matriz_aleatoria,
    TSP,
)

# Generar matriz de costos
matriz = generar_matriz_aleatoria(5)

print("Matriz de costos:")

for fila in matriz:
    print(fila)

# Crear instancia del problema
tsp = TSP(matriz)

# Generar ruta aleatoria
ruta = tsp.generar_ruta()

print("\nRuta inicial:", ruta)

# Calcular costo de la ruta
costo = tsp.calcular_costo(ruta)

print("Costo inicial:", costo)

# Optimización con 2-OPT
nueva_ruta, nuevo_costo = tsp.dos_opt(ruta)

print("\nRuta optimizada:", nueva_ruta)
print("Nuevo costo:", nuevo_costo)
```
---

# Pruebas unitarias

El proyecto incluye pruebas unitarias utilizando `pytest`.

Para ejecutarlas:

```bash
! pytest
```

Las pruebas verifican:

- validación de entradas
- generación de instancias
- cálculo correcto de soluciones
- funcionamiento de heurísticas
- optimización de rutas

---

# Libreta de ejemplos

El proyecto incluye una libreta de Jupyter con ejemplos completos de uso:

```text
examples/ejemplos_heuristicos.ipynb
```

La libreta contiene:

- ejemplos ejecutables
- explicación de algoritmos
- demostraciones prácticas
- pruebas de funcionamiento

---

# Tecnologías utilizadas

- Python 3
- Pytest
- Google Colab
- GitHub
- Jupyter Notebook

---

# Equipo de trabajo

- Jose Rodolfo De la Cruz Flores
- Carlos Perusi Hernandez Cuellar
- Marcela Mendoza Roque

---

# Licencia

Este proyecto fue desarrollado con fines académicos y educativos.

