# Voltear pancakes
def girar(pancakes, i):
    return pancakes[:i+1][::-1] + pancakes[i+1:]

# Revisar orden
def ordenado(pancakes):
    return all(pancakes[i] <= pancakes[i+1] for i in range(len(pancakes)-1))

# Función de búsqueda IDA
def ida(pancakes, heuristica, threshold):
    camino = []
    costo = heuristica(pancakes)
    while costo < float('inf'):
        result, nuevo_costo = limite_cost(pancakes, camino, costo, heuristica)
        if result is not None:
            return result
        # Actualizar el costo máximo
        costo = nuevo_costo
    return None

# Función de búsqueda DFS con límite de costo
def limite_cost(pancakes, path, costo, heuristica):
    # Obtener costo 
    f = len(path) + heuristica(pancakes)
    if f > costo:
        return None, f
    if ordenado(pancakes):
        return path, costo
    nuevo_costo = float('inf')
    nuevo_camino = None
    for i in range(len(pancakes)):
        nuevo_pancakes = girar(pancakes, i)
        nuevo_camino = path + [i+1]
        result, c = limite_cost(nuevo_pancakes, nuevo_camino, costo, heuristica)
        if result is not None:
            return result, costo
        nuevo_costo = min(nuevo_costo, c)
    return None, nuevo_costo

# Heuristica
def heuristica(pancakes):
    count = 0
    for i in range(len(pancakes)-1):
        if pancakes[i] > pancakes[i+1]:
            count += 1
    return count

# Ejemplo 
pancakes = [8, 3, 5, 4, 1, 2]
path = ida(pancakes, heuristica, 10)
print("Nodos recorridos:", len(path)+1)
print("Movimientos:", path)

# Resultado
pancakes_resuelto = pancakes
print("Estado inicial:", pancakes_resuelto)
for i in path:
    pancakes_resuelto = girar(pancakes_resuelto, i-1)
    print("Voltear los pancakes hasta el tamaño", i, ":", pancakes_resuelto)
print("Estado final:", pancakes_resuelto)


