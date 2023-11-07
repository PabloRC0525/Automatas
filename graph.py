'''# Clase para representar un objeto grafo
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # Una lista de listas para representar una lista adyacencia
        self.adjList = [[] for _ in range(n)]
        # Agrega bordes al grafo no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

# Prueba todas las combinaciones posibles de colores para cada nodo
def isSafe(g, color, v, c):
    for u in g.adjList[v]:
        if color[u] == c:
            return False
    return True

# Encuentra todas las K configuraciones coloreables del grafo
def KColoreable(g, color, k, v, n):
    if v == n:
        # Imprime la configuración de color actual
        print([COLORS[color[i]] for i in range(n)])
        return
    for c in range(k):
        if isSafe(g, color, v, c):
            color[v] = c
            KColoreable(g, color, k, v + 1, n)
            color[v] = None  # Restablece el color para volver a probar con otros colores

if __name__ == '__main__':
    # Lista de bordes del grafo
    edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
    # Lista para almacenar colores (puede manejar 10 grafos coloreables)
    COLORS = ['BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK', 'BLACK', 'BROWN', 'WHITE', 'PURPLE']
    # Establecer el número de vértices (nodos) en el grafo
    n = 6
    # Construir el grafo a partir de los datos anteriores
    g = Graph(edges, n)
    k = 3
    color = [None] * n
    # Imprime todas las K configuraciones coloreables del grafo
    KColoreable(g, color, k, 0, n)
    
'''   
class Graph:
    def __init__(self, edges, n):
        self.adj = [[] for _ in range(n+1)]
        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)

def isSafe(g, color, v, c):
    for u in g.adj[v]:
        if color[u] == c:
            return False
    return True

def kColorableWithColors(g, color, k, v, n, COLORS):
    if v == n+1:
        print([COLORS[col-1] for col in color[1:]])
        return
    for c in range(1, k + 1):
        if isSafe(g, color, v, c):
            color[v] = c
            kColorableWithColors(g, color, k, v + 1, n, COLORS)
            color[v] = 0

if __name__ == '__main__':
    COLORS = ['BLUE','GREEN','RED','YELLOW','ORANGE','PINK','BLACK','BROWN','WHITE','PURPLE']
    n = int(input("Ingrese el número de vértices: "))
    k = int(input("Ingrese el número de colores a evaluar: "))
    e = int(input("Ingrese el número de aristas: "))
    edges = []
    for i in range(e):
        src, dest = map(int,input("Ingrese la arista número "+str(i+1)+" (formato: src dest): ").split())
        edges.append((src, dest))
    g = Graph(edges, n)
    color = [None] * (n+1)
    kColorableWithColors(g, color, k, 1, n, COLORS)