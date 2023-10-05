import tkinter as tk
from tkinter import simpledialog

# Una clase para representar un conjunto disjunto
class DisjointSet:
    parent = {}

    # Realiza la operación MakeSet
    def make_set(self, n):
        # Crear n conjuntos disjuntos
        for i in range(n):
            self.parent[i] = i

    def find(self, k):
        if self.parent[k] == k:
            return k
        return self.find(self.parent[k])

    def union(self, a, b):
        # Encontrar la raíz de los conjuntos a los que pertenecen los elementos a y b
        x = self.find(a)
        y = self.find(b)

        self.parent[x] = y

# Función para construir el MST usando el algoritmo de Kruskal
def run_kruskal_algorithm(edges, n):
    MST = []

    # Inicializar la clase disjoint set
    # Crea un conjunto singleton para cada elemento del universo
    ds = DisjointSet()
    ds.make_set(n)
    index = 0

    # Ordena los bordes aumentando el peso
    edges.sort(key=lambda x: x[2])

    # MST contiene exactamente n-1 aristas
    while len(MST) != n - 1:
        # Considerar el borde siguiente con peso mínimo del grafo
        (src, dest, weight) = edges[index]
        index = index + 1

        # Encontrar la raíz de los conjuntos a los que se unen los dos extremos
        # Los vértices de la siguiente arista pertenecen

        x = ds.find(src)
        y = ds.find(dest)

        # Si ambos extremos tienen diferentes raíces, pertenecen a
        # diferentes componentes conectadas y se pueden incluir en MST

        if x != y:
            MST.append((src, dest, weight))
            ds.union(x, y)
    return MST

def obtener_datos_grafo():
    # Pedir al usuario los datos del grafo
    edges = []
    try:
        num_edges = int(simpledialog.askstring("Número de Aristas", "Ingrese el número de aristas:"))
        for i in range(num_edges):
            edge_data = simpledialog.askstring("Arista", f"Ingrese los datos de la arista {i + 1} (u, v, w):")
            u, v, w = map(int, edge_data.split(","))
            edges.append((u, v, w))
    except ValueError:
        tk.messagebox.showerror("Error", "Ingrese datos válidos para el grafo.")
        return None, None

    num_nodes = max(max(u, v) for u, v, _ in edges) + 1
    return edges, num_nodes

def main():
    # Crear una ventana Tkinter
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    # Obtener los datos del grafo
    edges, num_nodes = obtener_datos_grafo()
    if edges is None:
        return

    # Construir el MST
    e = run_kruskal_algorithm(edges, num_nodes)

    # Mostrar el resultado en la ventana
    result_str = "\n".join([f"({u}, {v}, {w})" for u, v, w in e])
    tk.messagebox.showinfo("Resultado", f"Árbol de Expansión Mínima (MST):\n{result_str}")

if __name__ == '__main__':
    main()
