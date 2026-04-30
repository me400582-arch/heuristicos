# Heurísticos

Paquete en Python que implementa algoritmos heurísticos para:

- Problema del Agente Viajero (TSP)
- Problema de la Mochila

## Instalación

```bash
pip install .

## Tests

Para ejecutar las pruebas:

```bash
pip install .[test]
pytest

## Uso

### Mochila Greedy

```python
from heuristicos_pkg.knapsack import mochila_greedy

valores = [60, 100, 120]
pesos = [10, 20, 30]

print(mochila_greedy(valores, pesos, 50))
