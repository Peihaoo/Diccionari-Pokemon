#Codi per netejar pantalla
import os
clear = lambda: os.system('cls')

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
    input("Introduce cualquier cosa para continuar...")

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
MODIFICAR_PALABRA = 1
MODIFICAR_DEFINICION = 2

AÑADIR_CONTENIDO = 3
AÑADIR_PALABRA = 1
AÑADIR_DEFINICION = 2

ELIMINAR_CONTENIDO = 4
ELIMINAR_PALABRA = 1
ELIMINAR_DEFINICION = 2

#VARIABLES
eleccioMenuPrincipal = -1
eleccioSecundaria = -1


while eleccioMenuPrincipal != 0:
    clear()
    eleccioMenuPrincipal = -1
    eleccioSecundaria = -1
    palabra = a
    #Menu Principal
    eleccioMenuPrincipal = menuPrincipal()
    
    match eleccioMenuPrincipal:
        #Sortir del programa
        case SALIR: print("Sortint...")
        #Mostrar informació
        case MOSTRAR_CONTENIDO: 
            eleccioSecundaria = menuMostrarInfo()
            if eleccioSecundaria == MOSTRAR_TODO:
                print(pokepedia)
            elif eleccioSecundaria == MOSTRAR_PALABRA:
                palabra = input("¿Qué palabra quieres mostrar?")
                if(palabra in pokepedia.keys()): 
                    a
                else: 
                    a
        #Modificar informació
        case MODIFICAR_CONTENIDO:
            eleccioSecundaria =
        #Añadir contenido
        case AÑADIR_CONTENIDO:
            eleccioSecundaria = 
        #Eliminar contenido
        case ELIMINAR_CONTENIDO:
            eleccioSecundaria = 
        #Opció no vàlida
        case _: print('Opcio no vàlida')
