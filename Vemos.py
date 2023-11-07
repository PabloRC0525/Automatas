#Crear un programa que use backtracking 
#Plantear un problema y su solución
#Restricciones:
#-No acceso a internet
#-No equipos de 3
#-No copilot
#No Chat GPT
#1500TC<19:00
#1000 TC<23:59
#Pareja ganadora excentan 2do parcial 
#2do lugar No hace tareas
#3er lugar 10 PB

import random
from itertools import product

def generar_maridaje_unico(vinos, alimentos):
    maridajes = []

    for vino, alimento in product(vinos, alimentos):
        maridajes.append((vino, alimento))

    random.shuffle(maridajes)
    return maridajes

if __name__ == "__main__":
    vinos = ["Vino Tinto", "Vino Blanco", "Champán", "Vino Rosado", "Chardonnay","Cabernet Sauvignon", "Sauvignon Blanc", "Syrah"]
    alimentos = ["Carne roja", "Pescado", "Queso curado", "Chocolte", "Pollo a la parrilla", "Ensalada Cesar", "Sushi", "Filete de res", "Pasta al pesto", "Risotto de champiñones"]

    numero_de_maridajes = 20
    
    maridajes = generar_maridaje_unico(vinos, alimentos)

    for i in range(numero_de_maridajes):
        vino, alimento = maridajes[i]
        print(f"Maridaje sugerido {i + 1}: {vino} con {alimento}")
