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

def kColorableWithColors(g, color, k, v, n, LIBROS, cant):
    if v == n+1:
        #print([LIBROS[col-1] for col in color[1:]])
        cant[0] += 1
        return
    for c in range(1, k + 1):
        if isSafe(g, color, v, c):
            color[v] = c
            kColorableWithColors(g, color, k, v + 1, n, LIBROS, cant)
            color[v] = 0
    return cant  
    

if __name__ == '__main__':
    LIBROS = ['100 años de soledad', 'Física', 'Cálculo', 'Inglés', 'L y A', 'I.O.O.P', 'Conmutación y ruteo']
    n = 8#int(input("Ingrese el número de vértices: "))
    k = 7#int(input("Ingrese el número de libros a evaluar: "))
    #e = 17#int(input("Ingrese el número de aristas: "))
    edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 3), (2, 4), (2, 7), (2, 8), (3, 7), (3, 5), (3, 6), (4, 8), (4, 5), (5, 7), (6, 8), (7, 8)]
    """ for i in range(e):
        src, dest = map(int,input("Ingrese la arista número "+str(i+1)+" (fuente 'espacio' destino): ").split())
        edges.append((src, dest)) """
    g = Graph(edges, n)
    color = [None] * (n+1)
    cant = [0]
    num = kColorableWithColors(g, color, k, 1, n, LIBROS, cant)
    print(num)