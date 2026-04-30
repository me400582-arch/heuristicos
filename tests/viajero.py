from heuristicos_pkg.tsp import vecino_mas_cercano

def test_tsp_basico():
    ciudades = [(0,0), (1,0), (0,1), (1,1)]
    ruta = vecino_mas_cercano(ciudades)

    assert len(ruta) == len(ciudades)
    assert len(set(ruta)) == len(ciudades)
