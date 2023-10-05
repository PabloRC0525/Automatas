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

def print_itinerary(dictionary, src):
    dest = dictionary.get(src)
    if not dest:
        return src
    return src + ' -> ' + print_itinerary(dictionary, dest)

def find_itinerary():
    input_text = input_entry.get("1.0", "end-1c")  # Obtiene el texto ingresado por el usuario
    input_lines = input_text.split('\n')
    tickets = {}
    
    for line in input_lines:
        if line:
            src, dest = line.strip().split(':')
            tickets[src] = dest

    # Encuentra el itinerario
    destinations = set(tickets.values())
    for k, v in tickets.items():
        if k not in destinations:
            initial_station = k
            itinerary = print_itinerary(tickets, k)
            final_station = v
            
            # Configurar etiquetas para mostrar estación inicial, final y el itinerario
            initial_label.config(text=f"Inicio: {initial_station}")
            final_label.config(text=f"Final: {final_station}")
            result_label.config(text=f"Itinerario: {itinerary}")
            break

# Crear ventana tkinter
root = tk.Tk()
root.title("Itinerario de Viaje")

# Crear cuadro de entrada
input_label = tk.Label(root, text="Ingrese los datos de destino (Formato: Origen:Destino):")
input_label.pack()
input_entry = tk.Text(root, height=5, width=30)
input_entry.pack()

# Botón para encontrar el itinerario
find_button = tk.Button(root, text="Encontrar Itinerario", command=find_itinerary)
find_button.pack()

# Etiquetas para mostrar la estación inicial, final y el itinerario
initial_label = tk.Label(root, text="")
initial_label.pack()
final_label = tk.Label(root, text="")
final_label.pack()
result_label = tk.Label(root, text="")
result_label.pack()

# Iniciar la aplicación tkinter
root.mainloop()
