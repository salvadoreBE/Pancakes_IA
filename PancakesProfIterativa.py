from copy import deepcopy

def pancakes(stack):
    """"
    Función que ordena un stack de pancakes
    utilizando una búsqueda en profundidad iterativa recursiva
    """
    # Definir una función que verifique si el stack está ordenado
    def ordenado(s):
        return all(s[i] <= s[i+1] for i in range(len(s)-1))
    
    # Definir una función que voltee los pancakes desde el inicio hasta la posición k
    def girar(s, k):
        return s[:k+1][::-1] + s[k+1:]

    # Definir una función auxiliar que realiza la búsqueda en profundidad iterativa recursiva
    def profundidad_iterativa_rec(s, max_d, path):
        if ordenado(s):
            return True
        if max_d == 0:
            return False
        for i in range(len(s)):
            nuevo_stack = girar(s, i)
            if nuevo_stack not in path:
                path.append(nuevo_stack)
                if profundidad_iterativa_rec(nuevo_stack, max_d - 1, path):
                    return True
                path.pop()
        return False
    
    # Realizar una búsqueda de profundidad iterativa recursiva con una profundidad máxima que aumenta
    for depth in range(1, len(stack)+1):
        path = [stack]
        if profundidad_iterativa_rec(deepcopy(stack), depth, path):
            return path
        
stack = ['d', 'b', 'c', 'a']
path = pancakes(stack)
for i, p in enumerate(path):
    print(f"Estado {i}: {p}")
print(f"Se necesitaron {len(path)-1} movimientos para ordenar el stack.")
