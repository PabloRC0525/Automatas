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

("Zeus",""),    
("Apolo","Zeus"), 
("Artemisa","Zeus"),
Apolo es el padre de Asclepio y Orfeo.
Artemisa es la madre de Hermes y Callisto.
Asclepio es el padre de Podalirio y Machaon.
Orfeo es el padre de Linus y Eurydice.
Hermes es el padre de Pan y Dionisio.
Callisto es la madre de Arcas y Iasion.
Podalirio es el padre de Machaon y Polidoro.
Machaon es el padre de Nireo y Nicomedes.
Eurydice es la madre de Gargareia y Argonautas.
Pan es el padre de Silenos y Eufeme.
Dionisio es el padre de Priapo y Ámpelo.
Arcas es el padre de Elato y Azeo.
Iasion es el padre de Demofonte y Pluto.
Polidoro es el padre de Peonio y Polifonte.
Nireo es el padre de Iofante y Pandaro.
Nicomedes es el padre de Linanto y Medonte.
Gargareia es la madre de Licaón y Cecropia.
Argonautas es el padre de Cánace y Estinfalo.
Silenos es el padre de Fauno y Marone.
Eufeme es la madre de Batus y Eurínome.
Priapo es el padre de Adono y Céfiro.
Ámpelo es el padre de Bromio y Oinopion.
Elato es el padre de Apolis y Toxeo.
Azeo es el padre de Carpo y Eufrósine.
Demofonte es el padre de Amintor y Cale.
Pluto es el padre de Zagreo y Íaco.
Peonio es el padre de Anficlea y Icario.
Polifonte es el padre de Bacis y Cometes.
Iofante es el padre de Sicino y Ceáfix.
Pandaro es el padre de Atymnius y Equeclea.
Linanto es el padre de Aleimón y Acestor.
Medonte es el padre de Lago y Capaneo.
Licaón es el padre de Nicomaco y Misipe.
Cecropia es la madre de Erecteo y Atenea.
Cánace es la madre de Linceo y Abante.
Estinfalo es el padre de Atys y Milón.
Fauno es el padre de Latínus y Tarquino.
Marone es el padre de Sileno y Milo.
Batus es el padre de Elatiades y Epeio.
Eurínome es la madre de Lacedemon y Gala.
Adono es el padre de Ninias y Agdistis.
Céfiro es el padre de Balio y Xanto.
Bromio es el padre de Liriope y Naso.
Oinopion es el padre de Ampelo y Tiro.
Carpo es la madre de Ascaio y Corinto.
Eufrósine es la madre de Cleta y Euforión.
Amintor es el padre de Emetes y Estesícoro.
Cale es la madre de Micceón y Lutro.
Zagreo es el padre de Ágave y Pantíno.
Íaco es el padre de Acasto y Pelias.
Anficlea es la madre de Milo y Bato.
Icario es el padre de Ersínoe y Ritmo.
Bacis es el padre de Cleoboea y Ismaro.
Cometes es el padre de Lelanto y Titono.
Sicino es el padre de Etolo y Sibaris.
Ceáfix es el padre de Toloso y Cécrope.
Atymnius es el padre de Aglao y Androgea.
Equeclea es la madre de Ergino y Periboea.
Aleimón es el padre de Pilos y Argeo.
Acestor es el padre de Poeas y Piritoo.
Lago es el padre de Clitio y Perieres.
Capaneo es el padre de Licofonte y Ilares.
Nicomaco es el padre de Alcmeón y Erato.
Misipe es la madre de Anaxibia y Astioquia.
Erecteo es el padre de Aglauro y Herse.
Atenea es la madre de Erictonio y Pandión.
Linceo es el padre de Abante y Eurícione.
Abante es el padre de Pero y Laódice.
Atys es el padre de Aglaura y Aglie.
Milón es el padre de Deifobo y Pródico.
Latínus es el padre de Silvius y Aventino.
Tarquino es el padre de Arúntio y Tanaquil.
Sileno es el padre de Fílira y Pegaso.
Milo es el padre de Astídamas y Tiagro.
Elatiades es el padre de Ameinias y Molon.
Epeio es el padre de Endeo y Toxeo.
Lacedemon es el padre de Dorio y Eurice.
Gala es la madre de Alexiada y Polydora.
Ninias es el padre de Cuidir y Polyxeño.
Agdistis es la madre de Circe y Acis.
Balio es el padre de Jocasta y Harmonía.
Xanto es el padre de Antígona y Ismene.
Liriope es la madre de Narciso y Melo.
Ampelo es el padre de Línea y Calcone.
Tiro es la madre de Neleo y Pelias.
Ascaio es la madre de Ateneo y Autoctona.
Corinto es el padre de Eunostos y Bellerofonte.
Cleta es la madre de Doris y Melite.
Euforión es el padre de Deífone y Danae.
Emetes es el padre de Psamathe y Echinades.
Estesícoro es el padre de Arete y Nicias.
Micceón es el padre de Hipseo y Sceus.
Lutro es el padre de Himera y Eryx.
Ágave es la madre de Penteo y Pirante.
Pantíno es el padre de Menesicle y Leocoridas.
Ersínoe es la madre de Butes y Crenaeus.
Ritmo es el padre de Tirreno y Carme.
Cleoboea es la madre de Clytie y Leucothea.
Ismaro es el padre de Marpessa y Hypsipyle.
Lelanto es el padre de Pegasides y Nereides.
Titono es el padre de Eos y Hemera.
Etolo es el padre de Leucippe y Thestius.
Sibaris es el padre de Hesperia y Iapyx.
Toloso es el padre de Gelone y Batis.
Cécrope es el padre de Europa y Cadmus.
Aglao es el padre de Lilaea y Podargos.
Androgea es la madre de Ceneo y Glanis.
Ergino es el padre de Corinna y Hípaso.
Periboea es la madre de Oeneus y Agrius.
Poeas es el padre de Philammon y Sarpedon.
Piritoo es el padre de Polidoro y Cleopatra.
Nicomaco es el padre de Andrómaca y Astianacte.
Misipe es la madre de Harmonia y Semele.
Aglauro es la madre de Cecrops y Erysichthon.
Erictonio es el padre de Pandión y Butes.
("Egeo","Pandión"), 
("Pallas","Pandión"),
("Heraclides","Cálice"), 
("Perseus","Cálice"),
("Bellerofonte", "Pegaso"),
("Melanipe" ,"Pegaso")
    
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

