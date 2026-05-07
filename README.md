# Heurísticos - Problema de la Mochila 0/1

Paquete en Python que implementa algoritmos heurísticos y exactos para resolver el Problema de la Mochila 0/1.

---

# Descripción

El problema de la mochila consiste en seleccionar objetos con cierto peso y valor para maximizar la ganancia total sin exceder la capacidad máxima de la mochila.

Este proyecto implementa tres enfoques diferentes:

- Greedy
- Backtracking
- Recocido Simulado

---

# Algoritmos implementados

## Greedy

Selecciona objetos según la mejor relación valor/peso.

- Rápido
- No siempre óptimo
- Complejidad aproximada: O(n log n)

---

## Backtracking

Explora todas las posibles combinaciones de objetos.

- Garantiza solución óptima
- Complejidad exponencial O(2^n)

---

## Recocido Simulado

Metaheurística inspirada en el enfriamiento de metales.

- Busca soluciones aproximadas
- Evita óptimos locales
- Usa aceptación probabilística

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
heuristicos_pkg/
│
├── heuristicos_pkg/
│   └── knapsack.py
│
├── tests/
│   └── test_knapsack.py
│
├── README.md
├── pyproject.toml
└── ejemplo.py
```

---

# Ejemplo de uso

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

# Ejecutar pruebas

Ejecutar los tests usando pytest:

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

# Licencia

Proyecto académico con fines educativos.
