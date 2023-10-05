'''
from random import randrange
def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp
def shuffle(A):
    for i in range(len(A)-1):
        j=randrange(i,len(A))
        swap(A,i,j)
if __name__=='__main__':
    A=[1,2,3,4,5,6]
    shuffle(A)
    print(A) 
    '''
import tkinter as tk
from random import randrange

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def shuffle(A):
    for i in range(len(A) - 1):
        j = randrange(i, len(A))
        swap(A, i, j)

data = []  # Definimos la lista data fuera de las funciones
num_data_to_enter = 0

def get_num_data():
    global num_data_to_enter
    num_data_to_enter = int(num_data_entry.get())
    data_window = tk.Toplevel(root)
    data_window.title("Ingresar Datos")

    data_label = tk.Label(data_window, text="Ingresa los datos uno por uno:")
    data_label.pack()

    data_entry = tk.Entry(data_window)
    data_entry.pack()

    def add_data():
        try:
            value = int(data_entry.get())
            if len(data) < num_data_to_enter:
                data.append(value)
                data_entry.delete(0, tk.END)
            else:
                data_entry.delete(0, tk.END)
                data_entry.insert(0, "Ya has ingresado suficientes datos.")
        except ValueError:
            pass

    add_button = tk.Button(data_window, text="Agregar Dato", command=add_data)
    add_button.pack()

    def shuffle_and_display():
        shuffle(data)
        result_window = tk.Toplevel(root)
        result_window.title("Datos Mezclados")

        result_label = tk.Label(result_window, text=', '.join(map(str, data)), font=("Arial", 12))
        result_label.pack()

    shuffle_button = tk.Button(data_window, text="Mezclar Datos", command=shuffle_and_display)
    shuffle_button.pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Mezclador de Datos")

# Crear una etiqueta y una entrada para ingresar el número de datos
num_data_label = tk.Label(root, text="Ingresa el número de datos:")
num_data_label.pack()

num_data_entry = tk.Entry(root)
num_data_entry.pack()

get_data_button = tk.Button(root, text="Continuar", command=get_num_data)
get_data_button.pack()

root.mainloop()
