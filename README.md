# Heurísticos 
# Problema de la Mochila 0/1

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
