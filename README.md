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

## Integrantes y módulos

Este proyecto fue desarrollado en equipo.

### Módulo Mochila 0/1

Implementación de algoritmos heurísticos y exactos:

* Greedy
* Backtracking
* Recocido Simulado

### Módulo Agente Viajero

(Esta sección será completada por el integrante encargado del módulo del agente viajero.)

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

* José Rodolfo de la Cruz Flores
* Marcela Mendoza Roque
* Carlos Perusi Hernandez Hernandez

---

## Licencia

Proyecto académico desarrollado con fines educativos.
