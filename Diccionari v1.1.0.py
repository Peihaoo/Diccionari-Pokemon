#Codi per netejar pantalla
import os
clear = lambda: os.system('cls')

#Creació del diccionari amb 3 entrades bàsiques
pokepedia = {
    "tiposElementales":{
        "NORMAL": "Los tipos normal son los más diversos entre los Pokémon, es el tipo de los normies, hay una gran cantidad de normies en el mundo pokemon, es el tipo elemental más comun. "
    },
    "pokedex":{
        "RATATA": "TIPO: NORMAL. Una ratilla que te encuentras hasta bajo las piedras, literalmente."
    },
    "ataques":{
        "PLACAJE": "TIPO: NORMAL. Corre (o no) hacia ti y te pega con su cuerpo."
    },
}
#DEFINES
SALIR = 0

MOSTRAR_CONTENIDO = 1
MOSTRAR_TODO = 1
MOSTRAR_PALABRA = 2

MODIFICAR_CONTENIDO = 2
MODIFICAR_APARTADO = 1
MODIFICAR_PALABRA = 2

AÑADIR_CONTENIDO = 3
AÑADIR_APARTADO = 1
AÑADIR_PALABRA = 2

ELIMINAR_CONTENIDO = 4
ELIMINAR_APARTADO = 1
ELIMINAR_PALABRA = 2

#VARIABLES
eleccioMenuPrincipal = -1
eleccioSecundaria = -1

#Funcions
def menuPrincipal():
    print("Hola, bienvenido a la pokepedia.¿Qué quieres hacer?")
    print(str(MOSTRAR_CONTENIDO) + ". Ver contenido de la Pokepedia.")
    print(str(MODIFICAR_CONTENIDO) + ". Modificar contenido de la Pokepedia.")
    print(str(AÑADIR_CONTENIDO) + ". Añadir contenido a la Pokepedia.")
    print(str(ELIMINAR_CONTENIDO) + ". Eliminar contenido de la Pokepedia.")
    print(str(SALIR) + ". Salir de la Pokepedia.")
    return int(input("Introduce tu eleccion: "))

def menuMostrarInfo():
    print("¿Qué quieres mostrar?")
    print(str(MOSTRAR_TODO) + ". Toda la Pokepedia.")
    print(str(MOSTRAR_PALABRA) + ". Solo las entradas de una palabra.")
    return int(input("Introduce tu eleccion: "))

def getch():
    input("\nIntroduce cualquier cosa para continuar...")

def mostrarPalabra():
    clear()
    palabra = input("¿Qué palabra quieres mostrar? ")
    clear()
    if palabra in pokepedia.keys(): 
        print(pokepedia[palabra])
        getch()
    else: 
        print("Palabra no encontrada.")
        getch()

def menuModificarInfo():
    print("¿Qué quieres modificar?")
    print(str(MODIFICAR_APARTADO) + ". Nombre de un apartado.")
    print(str(MODIFICAR_PALABRA) + ". Definicion de una palabra.")
    return int(input("Introduce tu eleccion: "))
def modificarApartado():
    clear()
    apartado = input("¿Qué apartado quieres modificar? ")
    clear()
    if apartado in pokepedia.keys():
        nuevoApartado = input("Cómo quieres renombrarlo? ")
        pokepedia[nuevoApartado] = pokepedia.pop(apartado)
        print("'"+ apartado + "' fue renombrado a '" + nuevoApartado + "' con éxito.")
        getch()
    else:
        print("El apartado introducido no existe.")
        getch()

def modificarPalabra():
    clear()
    apartado = input("¿De qué apartado es la palabra que quieres modificar? ")
    palabra = input("Qué palabra quieres modificar? ")
    clear()
    if palabra in pokepedia.get(apartado, {}):
        nuevaDefinicion = input("Introduce la nueva definicion de la palabra '" + palabra + "': ")
        pokepedia[apartado][palabra] = nuevaDefinicion
        pokepedia[palabra] = nuevaDefinicion
        print("Definicion modificada con éxito.")
        getch()
    else:
        print("La palabra introducida no existe.")
        getch()

def entradaMenusSecundaris(eleccioMenuPrincipal):
    match eleccioMenuPrincipal:
        #Sortir del programa
        case x if eleccioMenuPrincipal == SALIR: print("Saliendo...")
        #Mostrar informació
        case x if eleccioMenuPrincipal == MOSTRAR_CONTENIDO: 
            eleccioSecundaria = menuMostrarInfo()
            if eleccioSecundaria == MOSTRAR_TODO:
                clear()
                print(pokepedia)
                getch()
            elif eleccioSecundaria == MOSTRAR_PALABRA:
                mostrarPalabra()
        #Modificar informació
        case x if eleccioMenuPrincipal == MODIFICAR_CONTENIDO:
            eleccioSecundaria = menuModificarInfo()
            if eleccioSecundaria == MODIFICAR_APARTADO:
                modificarApartado()
            elif eleccioSecundaria == MODIFICAR_PALABRA:
                modificarPalabra()
        #Añadir contenido
        case x if eleccioMenuPrincipal == AÑADIR_CONTENIDO:
            eleccioSecundaria = 1
        #Eliminar contenido
        case x if eleccioMenuPrincipal == ELIMINAR_CONTENIDO:
            eleccioSecundaria = 1
        #Opció no vàlida
        case _: print('Opcio no vàlida')

#Main
while eleccioMenuPrincipal != 0:
    clear()
    eleccioMenuPrincipal = -1
    eleccioSecundaria = -1
    palabra = "a"
    #Menu Principal
    eleccioMenuPrincipal = menuPrincipal()
    clear()
    entradaMenusSecundaris(eleccioMenuPrincipal)
