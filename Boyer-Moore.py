'''#funcion para encontarr el elmento mayoritario presente en una lista dad
def findMajorityElement(nums):
    #crear un hashmap vacio
    d={}
    #almacena la  frecuencia de cada elemento en un diccionario
    for i in nums:
        d[i]=d.get(i,0) + 1
    #devuelve el elemento si se cuenta es mayor que n/2
    for key, value in d.items():
        if value > len(nums)/2:
            return key
    #ningun elemento mayoritario esta presente
    return-1

if __name__ == '__main__':

#suposicion # entrada valida (el elemento mayoritario esta presente)
    nums=[1,8,7,4,1,2,2,2,2,2,2]
    result=findMajorityElement(nums)
    if result !=-1:
        print('El elemento mayoritario es:', result)
    else:
        print('The majority element doesnt exist')

        #pedir datos usando tkinter
        #parametrso de entrada y salida
        #cuantos datos tienes
        #ingresar datos 1,2,3 ,n'''

import tkinter as tk
from tkinter import simpledialog, messagebox

# Función para encontrar el elemento mayoritario presente en una lista dada
def encontrarElementoMayoritario(lista):
    if not lista:
        return None

    # Crear un diccionario vacío
    conteo = {}

    # Calcular el conteo de cada elemento en la lista
    for elemento in lista:
        if elemento in conteo:
            conteo[elemento] += 1
        else:
            conteo[elemento] = 1

    # Encontrar el elemento con el mayor conteo
    elemento_mayoritario = max(conteo, key=conteo.get)
    conteo_mayoritario = conteo[elemento_mayoritario]

    # Verificar si el elemento con mayor conteo es mayoritario
    if conteo_mayoritario > len(lista) / 2:
        return elemento_mayoritario
    else:
        return None

# Función para manejar el botón "Calcular"
def calcular():
    # Obtener la cantidad de datos del usuario
    cantidad_datos = entrada_cantidad_datos.get()
    try:
        cantidad_datos = int(cantidad_datos)
        if cantidad_datos <= 0:
            messagebox.showerror("Error", "La cantidad de datos debe ser mayor que 0.")
            return
    except ValueError:
        messagebox.showerror("Error", "La cantidad de datos debe ser un número entero.")
        return

    # Pedir al usuario que ingrese la lista de elementos
    entrada_lista = simpledialog.askstring("Ingresar Lista", "Ingrese la lista de elementos (separados por comas):")
    if entrada_lista is None:
        return

    # Separar la entrada en una lista de elementos
    lista = entrada_lista.split(',')

    # Eliminar espacios en blanco alrededor de los elementos
    lista = [elemento.strip() for elemento in lista]

    # Verificar si la cantidad de datos ingresados coincide con la cantidad especificada
    if len(lista) != cantidad_datos:
        messagebox.showerror("Error", f"La cantidad de datos ingresados ({len(lista)}) no coincide con la cantidad especificada ({cantidad_datos}).")
        return

    # Llamar a la función para encontrar el elemento mayoritario
    resultado = encontrarElementoMayoritario(lista)

    if resultado is not None:
        resultado_label.config(text=f'El elemento mayoritario es: {resultado}')
    else:
        resultado_label.config(text='No existe un elemento mayoritario')

# Crear una ventana Tkinter
ventana = tk.Tk()
ventana.title("Encontrar Elemento Mayoritario")

# Etiqueta y entrada para ingresar la cantidad de datos
etiqueta_cantidad_datos = tk.Label(ventana, text="Ingrese la cantidad de datos:")
etiqueta_cantidad_datos.pack()
entrada_cantidad_datos = tk.Entry(ventana)
entrada_cantidad_datos.pack()

# Botón "Siguiente"
siguiente_boton = tk.Button(ventana, text="Siguiente", command=calcular)
siguiente_boton.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()
