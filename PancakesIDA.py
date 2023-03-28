# Voltear pancakes
def girar(pancakes, i):
    return pancakes[:i+1][::-1] + pancakes[i+1:]

# Revisar orden
def ordenado(pancakes):
    return all(pancakes[i] <= pancakes[i+1] for i in range(len(pancakes)-1))

# Función de búsqueda IDA recursiva
def ida_rec(pancakes, heuristica, threshold):
    camino = []
    costo = heuristica(pancakes)
    return buscar_rec(pancakes, camino, costo, heuristica, threshold)

# Función auxiliar para buscar recursivamente
def buscar_rec(pancakes, camino, costo, heuristica, threshold):
    if costo > threshold:
        return None
    if ordenado(pancakes):
        return camino
    nuevo_costo = float('inf')
    for i in range(len(pancakes)):
        nuevo_pancakes = girar(pancakes, i)
        nuevo_camino = camino + [chr(i + 65)]
        nuevo_costo = min(nuevo_costo, heuristica(nuevo_pancakes) + len(nuevo_camino))
        result = buscar_rec(nuevo_pancakes, nuevo_camino, costo + 1, heuristica, threshold)
        if result is not None:
            return result
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
        nuevo_camino = path + [chr(i + 65)]
        result, c = limite_cost(nuevo_pancakes, nuevo_camino, costo, heuristica)
        if result is not None:
            return result, costo
        nuevo_costo = min(nuevo_costo, c)
    return None, nuevo_costo

# Heuristica
def heuristica(pancakes):
    count = 0
    for i in range(len(pancakes)-1):
        if ord(pancakes[i]) > ord(pancakes[i+1]):
            count += 1
    return count

# Ejemplo
pancakes = ['d', 'b', 'c', 'a']
path = ida_rec(pancakes, heuristica, 10)
print("Nodos recorridos:", len(path)+1)
print("Movimientos:", path)

# Resultado
pancakes_resuelto = pancakes
print("Estado inicial:", pancakes_resuelto)
for i in path:
    index = ord(i) - 65
    pancakes_resuelto = girar(pancakes_resuelto, index)
    print("Voltear los pancakes hasta el tamaño", i, ":", pancakes_resuelto)
print("Estado final:", pancakes_resuelto)



