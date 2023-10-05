import tkinter as tk
import random

# Definir los palos y los valores de la baraja inglesa
palos = ['Picas', 'Corazones', 'Diamantes', 'Tréboles']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Crear una baraja con todas las cartas
baraja = [{'valor': valor, 'palo': palo} for valor in valores for palo in palos]

# Función para repartir cartas a los jugadores
def repartir_cartas():
    num_jugadores = int(num_jugadores_entry.get())
    
    if 2 <= num_jugadores <= 4:
        # Revolver la baraja antes de repartir
        random.shuffle(baraja)
        
        # Crear una lista de manos para cada jugador
        manos = [[] for _ in range(num_jugadores)]
    
        # Repartir 7 cartas secuenciales a cada jugador
        for _ in range(7):
            for jugador in range(num_jugadores):
                carta = baraja.pop()
                manos[jugador].append(carta)
    
        # Mostrar las cartas restantes en la baraja
        cartas_restantes = [f"{carta['valor']} de {carta['palo']}" for carta in baraja]
        cartas_restantes_text.config(state=tk.NORMAL)  # Habilitar la edición del widget de texto
        cartas_restantes_text.delete(1.0, tk.END)  # Borrar el contenido existente
        cartas_restantes_text.insert(tk.END, "\n".join(cartas_restantes))  # Insertar cartas restantes
        cartas_restantes_text.config(state=tk.DISABLED)  # Deshabilitar la edición del widget de texto
    
        # Mostrar las manos de los jugadores en la ventana
        for jugador, mano in enumerate(manos):
            cartas_jugador = [f"{carta['valor']} de {carta['palo']}" for carta in mano]
            mano_label = tk.Label(root, text=f'Jugador {jugador + 1}: {", ".join(cartas_jugador)}', wraplength=300)
            mano_label.pack()
    else:
        cartas_restantes_text.config(state=tk.NORMAL)
        cartas_restantes_text.delete(1.0, tk.END)
        cartas_restantes_text.insert(tk.END, "Número de jugadores debe ser 2, 3 o 4.")
        cartas_restantes_text.config(state=tk.DISABLED)

# Crear la ventana principal
root = tk.Tk()
root.title("Repartidor de Cartas")

# Etiqueta y entrada para el número de jugadores
num_jugadores_label = tk.Label(root, text="Número de jugadores (2-4):")
num_jugadores_label.pack()

num_jugadores_entry = tk.Entry(root)
num_jugadores_entry.pack()

# Botón para repartir cartas
repartir_button = tk.Button(root, text="Repartir Cartas", command=repartir_cartas)
repartir_button.pack()

# Widget de texto para mostrar las cartas restantes

num_jugadores_label = tk.Label(root, text="Cartas restantes:")
num_jugadores_label.pack()
cartas_restantes_text = tk.Text(root, height=10, width=40, state=tk.DISABLED, wrap=tk.WORD)
cartas_restantes_text.pack()

num_jugadores_label = tk.Label(root, text="Repartición:")
num_jugadores_label.pack()
root.mainloop()

