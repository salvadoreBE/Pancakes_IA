import heapq
from typing import List, Tuple

# Obtener los vecinos
def vecinos(state: List[str]) -> List[List[str]]:
    n = len(state)
    vecinos = []
    for i in range(2, n + 1):
        nuevo_estado = state[:i][::-1] + state[i:]
        vecinos.append(nuevo_estado)
    return vecinos

# Obtener el costo de un movimiento
def costos(state: List[str], next_state: List[str]) -> int:
    return len(state) - len(next_state) + 1

# Valor heurístico de un estado
def heuristica(state: List[str], goal: List[str]) -> int:
    return sum([1 for i in range(len(state)) if state[i] != goal[i]])

# Función para resolver el juego de los pancakes con A*
def pancake_a_estrella(start: List[str], goal: List[str]) -> Tuple[int, List[List[str]]]:
    open_set = [(heuristica(start, goal), 0, start, [])]
    closed_set = set()
    while open_set:
        # Obtener el estado con menor costo total
        f, g, state, path = heapq.heappop(open_set)
        if state == goal:
            return g, path + [state]
        if tuple(state) in closed_set:
            continue
        closed_set.add(tuple(state))
        neighbors = vecinos(state)
        for next_state in neighbors:
            if tuple(next_state) not in closed_set:
                new_path = path + [state]
                new_g = g + costos(state, next_state)
                new_f = new_g + heuristica(next_state, goal)
                heapq.heappush(open_set, (new_f, new_g, next_state, new_path))
    return -1, []

# Ejemplo
start = ['d', 'b', 'c', 'a']
goal = sorted(start)
cost, path = pancake_a_estrella(start, goal)
if cost == -1:
    print("No se encontró solución.")
else:
    print("Costo total: ", cost)
    print("Camino: ")
    for state in path:
        print(state)
