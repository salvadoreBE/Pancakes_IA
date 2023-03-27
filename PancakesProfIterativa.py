from copy import deepcopy

def pancakes(stack):
    """"
    Función que ordena un stack de pancakes
    utilizando una búsqueda en profundidad iterativa
    """
    # Definir una función que verifique si el stack está ordenado
    def ordenado(s):
        return all(s[i] <= s[i+1] for i in range(len(s)-1))
    
    # Definir una función que voltee los pancakes desde el inicio hasta la posición k
    def girar(s, k):
        return s[:k+1][::-1] + s[k+1:]

    def profundiad_iterativa(s, d, max_d, path):
        if ordenado(s):
            return True
        if d == max_d:
            return False
        for i in range(len(s)):
            nuevo_stack = girar(s, i)
            if nuevo_stack not in path:
                path.append(nuevo_stack)
                
                # Nueva busqueda en profundidad
                if profundiad_iterativa(nuevo_stack, d+1, max_d, path):
                    return True
                path.pop()
        
        # Si no se han encontrado soluciones
        return False
    
    # Realizar una búsqueda de profundidad iterativa con una profundidad máxima que aumenta
    for depth in range(1, len(stack)+1):
        path = [stack]
        if profundiad_iterativa(deepcopy(stack), 0, depth, path):
            return path
        
stack = [3, 1, 5, 2, 4, 8, 6]
path = pancakes(stack)
for i, p in enumerate(path):
    print(f"Estado {i}: {p}")
print(f"Se necesitaron {len(path)-1} movimientos para ordenar el stack.")
