from collections import deque

# Clase nodo
class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

    # Generar los nodos hijos
    def expand(self):
        hijos = []
        for i in range(2, len(self.state) + 1):
            new_state = self.state[:i][::-1] + self.state[i:]
            hijos.append(Node(new_state, self, f"flip({i})"))
        return hijos

# Definir metodo de busqueda de profundidad normal
def busqueda_profundidad(initial_state, goal_state):
    start_node = Node(initial_state)
    if start_node.state == goal_state:
        return start_node

    frontier = deque([start_node])
    explored = set()

    while frontier:
        node = frontier.pop()
        explored.add(tuple(node.state))

        for hijo in node.expand():
            if tuple(hijo.state) not in explored:
                if hijo.state == goal_state:
                    return hijo
                frontier.append(hijo)

    return None

def movimientos(node):
    actions = []
    while node.action:
        actions.append(node.action)
        node = node.parent
    return actions[::-1]

def print_state(state):
    print("[" + " ".join(str(s) for s in state) + "]")

# Ejemplo de uso
initial_state = [3, 1, 4, 2]
goal_state = [1, 2, 3, 4]

solution_node = busqueda_profundidad(initial_state, goal_state)

if solution_node:
    print("Movimientos")
    for action in movimientos(solution_node):
        print(action)
    print("Pancakes iniciales:")
    print_state(initial_state)
    print("Pancakes ordenados:")
    print_state(goal_state)
else:
    print("No se encontró solución.")








