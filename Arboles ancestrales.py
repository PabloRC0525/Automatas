class Persona:
    def __init__(self, nombre, padre=None):
        self.nombre = nombre
        self.padre = padre
        self.descendientes = []

    def agregar_descendiente(self, descendiente):
        self.descendientes.append(descendiente)

def crear_arbol():
    nombre_raiz = "Xavier"
    raiz = Persona(nombre_raiz)
    agregar_descendientes(raiz)
    return raiz

def agregar_descendientes(persona):
    descendientes = [
    ("Xavier", ""),
    ("Emilio I", "Xavier"),
    ("Xavier II", "Xavier"),
    ("Harry", "Emilio I"),
    ("Juan", "Emilio I"),
    ("Pablo", "Xavier II"),
    ("Alan", "Xavier II"),
    ("Carlos", "Harry"),
    ("Patricio", "Harry"),
    ("Carla", "Juan"),
    ("Carlota", "Juan"),
    ("Domingo", "Pablo"),
    ("Atanasio", "Pablo"),
    ("Jorge", "Alan"),
    ("Rodrigo", "Alan"),
    ("Carlos II", "Carlos"),
    ("Carmen", "Carlos"),
    ("Gepeto", "Patricio"),
    ("Victor", "Patricio"),
    ("Guadalupe", "Carlota"),
    ("Petra", "Atanasio"),
    ("Adrian", "Jorge"),
    ("Cesaria", "Rodrigo"),
    ("Helena", "Rodrigo"),
    ("Carlos III", "Carlos II"),
    ("Karol", "Carmen"),
    ("Carola", "Carmen"),
    ("Lucero", "Guadalupe"),
    ("Andres", "Guadalupe"),
    ("Fernando", "Adrian"),
    ("Ricardo", "Adrian"),
    ("Misael", "Helena"),
    ("Claudia", "Helena"),
    ("Larry", "Lucero"),
    ("Kevin", "Misael"),
    ("Santiago", "Claudia"),
    ("Britany", "Claudia")
    ]

    for nombre, padre in descendientes:
        if padre == persona.nombre:
            descendiente = Persona(nombre, padre=persona)
            persona.agregar_descendiente(descendiente)
            agregar_descendientes(descendiente)

def imprimir_arbol(persona, nivel=0):
    print("  " * nivel + persona.nombre)
    for descendiente in persona.descendientes:
        imprimir_arbol(descendiente, nivel + 1)

def buscar_persona(nombre, persona):
    if persona.nombre == nombre:
        return persona
    for descendiente in persona.descendientes:
        resultado = buscar_persona(nombre, descendiente)
        if resultado is not None:
            return resultado
    return None

def encontrar_ancestro_comun(persona1, persona2):
    ancestros1 = set()
    while persona1.padre is not None:
        ancestros1.add(persona1.padre.nombre)
        persona1 = persona1.padre

    while persona2.padre is not None:
        if persona2.padre.padre and persona2.padre.padre.nombre in ancestros1:
            return persona2.padre.padre.nombre
        persona2 = persona2.padre

    return None

arbol = crear_arbol()
imprimir_arbol(arbol)

while True:
    num_personas = int(input("¿Cuántas personas quieres buscar? "))
    nombres = [input(f"Ingresa el nombre de la persona {i+1}: ") for i in range(num_personas)]

    personas = [buscar_persona(nombre, arbol) for nombre in nombres]

    if None in personas:
        print("Uno o más nombres no se encuentran en el árbol.")
    else:
        ancestro_comun = encontrar_ancestro_comun(*personas[:2])
        if ancestro_comun is not None:
            print(f"El ancestro común más cercano de {', '.join(nombres)} es {ancestro_comun}.")
        else:
            print(f"{', '.join(nombres)} no tienen un ancestro común en este árbol.")

