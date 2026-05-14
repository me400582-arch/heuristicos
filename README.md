# Heurísticos

## Problemas de Optimización Combinatoria

Paquete en Python que implementa algoritmos heurísticos y exactos para resolver problemas clásicos de optimización combinatoria:

* Problema de la Mochila 0/1
* Problema del Agente Viajero (TSP)

---

## Descripción

Este proyecto desarrolla una biblioteca en Python orientada a la resolución de problemas clásicos de optimización combinatoria mediante distintos enfoques algorítmicos.

El objetivo principal es comparar algoritmos exactos y heurísticos, analizando su eficiencia computacional, complejidad y calidad de solución.

Actualmente incluye implementaciones para:

* Mochila 0/1
* Agente Viajero

---

## Problema de la Mochila 0/1

El problema de la mochila consiste en seleccionar objetos con peso y valor asociados para maximizar el beneficio total sin exceder una capacidad límite.

Se denomina **0/1** porque cada objeto tiene únicamente dos posibles estados:

* **0:** No se selecciona
* **1:** Se selecciona completamente

No es posible seleccionar fracciones de un objeto.

---

### Módulo 
Mochila 0/1

Implementación de algoritmos heurísticos y exactos:

* Greedy
* Backtracking
* Recocido Simulado

### Agente Viajero

Un vendedor debe de visitar un conjunto de $n$ ciudades, partiendo de una ciudad inicial, visitando cada ciudad exactemente una vez, finalmente regresando a la ciudad de origen. El objetivo es minimizar la distancia total recorrida o el costo.

---


### Módulo 

* Cruce Parcialmente Emparejado
* Búsqueda Local 2-OPT 
* Algoritmo Genético Completo para TSP 

---


## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/me400582-arch/heuristicos
```

Entrar al proyecto:

```bash
cd heuristicos
```

Instalar el paquete:

```bash
pip install .
```

---

## Estructura del proyecto

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

## Algoritmos implementados

### Greedy

Selecciona objetos utilizando la mejor relación valor/peso.

**Características:**

* Algoritmo heurístico
* Complejidad aproximada `O(n log n)`
* Rápido
* No siempre garantiza solución óptima

---

### Backtracking

Explora todas las combinaciones posibles.

**Características:**

* Algoritmo exacto
* Garantiza solución óptima
* Complejidad exponencial `O(2^n)`

---

### Recocido Simulado

Metaheurística inspirada en el enfriamiento de metales.

**Características:**

* Permite escapar de óptimos locales
* Usa aceptación probabilística
* Soluciones aproximadas eficientes

---
### Cruce Parcialmente Emparejado
En este algoritmo busca perservar la validez de las permutaciones, manteniendo el orden relativo, es biyectivo volvieendo fácil de implemetar.

**Caracteristicas:**
* Algoritmo combinatorio.
* Complejiad  O(n^2).
* Garantiza una biyección completa.
---

### Búsqueda Local 2-OPT 
 Elimina cruces en una ruta mediante el intercambio sistemático de pares de aristas.

**Caracteristicas:**
* Busqueda local.
* Complejidad Temporal O(n^2) y O(n^3)
* n > 1000, puede ser muy lento 
  
---
### Algoritmo Genético Completo para TSP:
A través de operadores como el cruce (PMX) y la mutación, se generan nuevas rutas,
manteniendo diversidad y evitando optimos locales.

**Caracteristicas:**
* Mejora garantizada en cada paso (monótono)
* No escala bien para grandes instancias (n > 1000)
* Intuitivo: elimina cruces no deseados en la ruta
* Puede quedar atrapado en óptimos locales de baja calidad

---

## Ejemplo de uso

Puedes modificar libremente los parámetros del problema para probar distintas instancias.

```python
from heuristicos_pkg.knapsack import mochila_greedy

valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidad = 50

seleccion, valor = mochila_greedy(valores, pesos, capacidad)

print("Selección:", seleccion)
print("Valor total:", valor)
```

También puedes agregar más objetos:

```python
valores = [60, 100, 120, 80, 200]
pesos = [10, 20, 30, 15, 40]
capacidad = 70
```

**Nota:**
Las listas `valores` y `pesos` deben tener la misma longitud.

---

## Ejecutar pruebas

Ejecutar las pruebas unitarias utilizando pytest:

```bash
pytest
```

Las pruebas verifican:

* Factibilidad de soluciones
* Correctitud del algoritmo exacto
* Consistencia del recocido simulado

---

## Tecnologías utilizadas

* Python
* Pytest
* GitHub
* LaTeX

---

## Equipo de trabajo

* De la cruz Flores Jose Rodolfo
* Marcela Mendoza Roque
* Carlos Perusi Hernandez Hernandez

---

## Licencia

Proyecto académico desarrollado con fines educativos.
