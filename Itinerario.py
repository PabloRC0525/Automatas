'''
def print_itinerary(dictionary,src):
    dest=dictionary.get(src)
    if not dest:
        return
    print(src+'->'+dest)
    print_itinerary(dictionary,dest)
def finditinerary(tickets):
    destinations={*tickets.values()}
    for k, v in tickets.items():
        if k not in destinations:
            print_itinerary(tickets,k)
            return
if __name__=='__main__':
    tickets={
            'LAX':'DXB',
            'DFW':'JFK',
            'LHR':'DFW',
            'JFK':'LAX'
        }
    finditinerary(tickets)
    '''

import tkinter as tk
import networkx as nx

def find_shortest_path():
    user_tickets = tickets_entry.get("1.0", "end-1c")  # Obtener los tickets ingresados por el usuario
    user_tickets = [line.strip() for line in user_tickets.split("\n") if line.strip()]  # Convertirlos a una lista de líneas
    
    # Crear un grafo dirigido a partir de los tickets
    G = nx.DiGraph()
    for line in user_tickets:
        src, dest = map(str.strip, line.split("->"))
        G.add_edge(src, dest)
    
    # Obtener la lista de trayectos ingresada por el usuario
    trayectos = trayectos_entry.get().split(',')
    
    # Verificar si hay al menos dos trayectos para calcular un camino
    if len(trayectos) < 2:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Debe ingresar al menos dos trayectos para calcular un camino.")
        return
    
    # Calcular el camino más corto
    shortest_path = []
    for i in range(len(trayectos) - 1):
        src = trayectos[i].strip()
        dest = trayectos[i + 1].strip()
        
        if not G.has_edge(src, dest):
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"No se encontró un camino de {src} a {dest}.")
            return
        
        shortest_path.extend(nx.shortest_path(G, source=src, target=dest, method='dijkstra')[:-1])
    
    # Mostrar el camino más corto en la interfaz gráfica
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Camino más corto:\n" + " -> ".join(shortest_path))

# Crear la ventana principal
window = tk.Tk()
window.title("Calcular Camino Más Corto")

# Etiqueta y entrada para los tickets personalizados (uno por línea)
tickets_label = tk.Label(window, text="Tickets personalizados (uno por línea):")
tickets_label.pack()
tickets_entry = tk.Text(window, height=5, width=40)
tickets_entry.pack()

# Etiqueta y entrada para los trayectos (separados por comas)
trayectos_label = tk.Label(window, text="Trayectos (separados por comas):")
trayectos_label.pack()
trayectos_entry = tk.Entry(window)
trayectos_entry.pack()

# Botón para calcular el camino más corto
calculate_button = tk.Button(window, text="Calcular Camino Más Corto", command=find_shortest_path)
calculate_button.pack()

# Resultados
result_text = tk.Text(window, height=10, width=40)
result_text.pack()

window.mainloop()

