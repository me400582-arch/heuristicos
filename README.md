# Heurísticos
# Problema de la Mochila 0/1

Paquete en Python que implementa algoritmos heurísticos y exactos para resolver el Problema de la Mochila 0/1.

---

# Descripción

El problema de la mochila consiste en seleccionar objetos con cierto peso y valor para maximizar la ganancia total sin exceder la capacidad máxima de la mochila.

Este proyecto implementa distintos enfoques heurísticos y exactos para resolver problemas clásicos de optimización combinatoria.

---

# Integrantes y módulos

Este proyecto fue desarrollado en equipo.

## Problema de la Mochila 0/1

Implementación de algoritmos heurísticos y exactos para el problema de la mochila:

- Greedy
- Backtracking
- Recocido Simulado

## Problema del Agente Viajero

(Esta sección será completada por el integrante encargado del módulo del agente viajero.)

---

# Instalación

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

# Estructura del proyecto

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
└── .gitignore
```

---

# Algoritmos implementados

## Greedy

Selecciona objetos utilizando la mejor relación valor/peso.

Características:

- Algoritmo heurístico
- Complejidad aproximada O(n log n)
- Rápido pero no siempre óptimo

---

## Backtracking

Explora todas las combinaciones posibles de objetos.

Características:

- Algoritmo exacto
- Garantiza solución óptima
- Complejidad exponencial O(2^n)

---

## Recocido Simulado

Metaheurística inspirada en el proceso de enfriamiento de metales.

Características:

- Permite escapar de óptimos locales
- Usa aceptación probabilística
- Obtiene soluciones aproximadas eficientes

---

# Ejecutar pruebas

Ejecutar los tests utilizando pytest:

```bash
pytest
```

---

# Tecnologías utilizadas

- Python
- Pytest
- GitHub
- LaTeX

---

# Equipo de trabajo

- De la Cruz Flores Jose Rodolfo
- Mendoza Roque Marcela
- Hernandez Cuellar Carlos Perusi

---

# Licencia

Proyecto académico con fines educativos.
