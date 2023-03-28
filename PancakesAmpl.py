from queue import Queue
from copy import deepcopy

def girar_panqueques(pila, n):
    return pila[:n][::-1] + pila[n:]

def ordenar_pila(pila):
    return all(pila[i] <= pila[i+1] for i in range(len(pila)-1))

# Función de búsqueda en amplitud
def busqueda_amplitud(pila):
    cola = Queue()
    cola.put((pila, []))
    visitados = set()
    visitados.add(tuple(pila))

    while not cola.empty():
        pila_actual, movimientos = cola.get()
        if ordenar_pila(pila_actual):
            return pila_actual, movimientos
        for i in range(2, len(pila_actual)+1):
            nueva_pila = girar_panqueques(pila_actual, i)
            if tuple(nueva_pila) not in visitados:
                nuevos_movimientos = movimientos + [nueva_pila]
                cola.put((nueva_pila, nuevos_movimientos))
                visitados.add(tuple(nueva_pila))
    
    # No se encontró una solución
    return None, None

# Ejemplo 
pila_inicial = ['d', 'b', 'c', 'a']
solucion, movimientos = busqueda_amplitud(pila_inicial)
if solucion is not None:
    print("Movimientos realizados para llegar al resultado:")
    for pila in movimientos:
        print(pila)
    print("El resultado:", solucion)
else:
    print("No se encontró una solución.")


