# Grafo inicial vacío
graph = {}

# Función para agregar un nodo al grafo
def add_node(graph, node):
    if node not in graph:
        graph[node] = []

# Función para agregar una arista (conexión) entre dos nodos
def add_edge(graph, node1, node2):
    if node1 in graph and node2 in graph:
        graph[node1].append(node2)
        graph[node2].append(node1)  # Para grafo no dirigido

# Función para mostrar el grafo
def display(graph):
    for node, edges in graph.items():
        print(f"{node}: {edges}")

# Ejemplo de uso
add_node(graph, 'A')
add_node(graph, 'B')
add_node(graph, 'C')
add_edge(graph, 'A', 'B')
add_edge(graph, 'A', 'C')
add_edge(graph, 'B', 'C')

print("Grafo:")
display(graph)
