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
MODIFICAR_DEFINICION = 3

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
def getch():
    #Funció pel getch()
    input("\nIntroduce cualquier cosa para continuar...")
    
def menuPrincipal():
    #Menu principal on selecciones què vols fer amb la Pokepedia
    print("Hola, bienvenido a la pokepedia.¿Qué quieres hacer?")
    print(str(MOSTRAR_CONTENIDO) + ". Ver contenido de la Pokepedia.")
    print(str(MODIFICAR_CONTENIDO) + ". Modificar contenido de la Pokepedia.")
    print(str(AÑADIR_CONTENIDO) + ". Añadir contenido a la Pokepedia.")
    print(str(ELIMINAR_CONTENIDO) + ". Eliminar contenido de la Pokepedia.")
    print(str(SALIR) + ". Salir de la Pokepedia.")
    
    return int(input("Introduce tu eleccion: "))

def menuMostrarInfo():
    #Menu per la mostra d'informació
    print("¿Qué quieres mostrar?")
    print(str(MOSTRAR_TODO) + ". Toda la Pokepedia.")
    print(str(MOSTRAR_PALABRA) + ". Solo las entradas de una palabra.")
    
    return int(input("Introduce tu eleccion: "))
    
def mostrarPalabra():
    #Mostrar només una paraula
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
    #Menu per la modificació d'informació
    print("¿Qué quieres modificar?")
    print(str(MODIFICAR_APARTADO) + ". Nombre de un apartado.")
    print(str(MODIFICAR_PALABRA) + ". Nombre de una palabra.")
    print(str(MODIFICAR_DEFINICION) + ". Definicion de una palabra.")
    
    return int(input("Introduce tu eleccion: "))
    
def modificarApartado():
    #Funció per modificar el nom d'un apartat
    clear()
    apartado = input("¿Qué apartado quieres modificar? ")
    clear()
    
    #Si la clau existeix a la Pokepedia:
    if apartado in pokepedia.keys():
        nuevoApartado = input("Cómo quieres renombrarlo? ")
        pokepedia[nuevoApartado] = pokepedia.pop(apartado)
        print("'"+ apartado + "' fue renombrado a '" + nuevoApartado + "' con éxito.")
        getch()
    else:
        print("El apartado introducido no existe.")
        getch()

def modificarPalabra():
    #Funció per modificar el nom d'una paraula
    clear()
    apartado = input("¿De qué apartado es la palabra que quieres modificar? ")
    palabra = input("Qué palabra quieres renombrar? ")
    nuevoNombre = input("A qué nombre quieres renombrarla? ")
    clear()
    
    #Si el valor de la clau existeix a la Pokepedia, li canviem el nom.
    if palabra in pokepedia.get(apartado, {}):
        #En aquest cas, creem una copia de la clau seleccionada per renombrar.
        pokepedia[apartado][nuevoNombre] = pokepedia[apartado][palabra]
        #I posteriorment eliminem la clau seleccionada per renombrar.
        del pokepedia[apartado][palabra]
    #Si no s'ha trobat dins de la Pokepedia, li comuniquem a l'usuari.
    else: 
        print("La palabra introducida no existe.")
        getch()
 
def modificarDefinicion():
    #Funció per modificar una definició
    clear()
    apartado = input("¿De qué apartado es la palabra que quieres modificar? ")
    palabra = input("Qué palabra quieres modificar? ")
    clear()
    
    #Si el valor de la clau existeix a la Pokepedia: 
    if palabra in pokepedia.get(apartado, {}):
        #Li preguntem a l'usuari per la nova definició
        nuevaDefinicion = input("Introduce la nueva definicion de la palabra '" + palabra + "': ")
        #Modifiquem la definició de la clau seleccionada
        pokepedia[apartado][palabra] = nuevaDefinicion
        print("Definicion modificada con éxito.")
        getch()
    #Si no s'ha trobat dins de la Pokepedia, li comuniquem a l'usuari.
    else:
        print("La palabra introducida no existe.")
        getch()

def menuAñadirInfo():
    #Menu d'adició de nova informació
    clear()
    print("¿Qué quieres añadir?")
    print(str(AÑADIR_APARTADO) + ". Un apartado. + palabra + definicion")
    print(str(AÑADIR_PALABRA) + ". Una palabra + su definicion.")
    
    return int(input("Introduce tu eleccion: "))

def añadirApartado():
    #Funció per afegir un apartat amb una paraula i definició
    clear()
    apartado = input("Cómo quieres que se llame el apartado? ")
    palabra = input("Qué palabra quieres añadir? ")
    definicion = input("Qué definicion tiene la palabra? ")
    
    #Afegim l'apartat amb la paraula i definició donada.
    pokepedia[apartado] = {palabra : definicion}
    clear()
    print("Apartado añadido con éxito.")
    getch()

def añadirPalabra():
    #Funció per afegir una paraula amb la seva definicio
    clear()
    apartado = input("A qué apartado quieres añadir la palabra? ")
    palabra = input("Qué palabra quieres añadir? ")
    definicion = input("Qué definicion tiene la palabra? ")
    
    #Si la clau existeix a la Pokepedia:
    if apartado in pokepedia.keys():
    #Afegim la paraula amb la definició donada dins de l'apartat especificat
        pokepedia[apartado].update({palabra:definicion})
        print("Palabra añadida con éxito.")
        getch()
    #Si no s'ha trobat dins de la Pokepedia, li comuniquem a l'usuari.    
    else:
        print("El apartado introducido no existe.")
        getch()

def menuEliminarInfo():
    #Menu per eliminar informació
    clear()
    print("Qué quieres eliminar?")
    print(str(ELIMINAR_APARTADO) + ". Un apartado entero.")
    print(str(ELIMINAR_PALABRA) + ". Una palabra.")
    
    return int(input("Introduce tu eleccion: "))
    
def eliminarApartado():
    #Funció per l'eliminació d'un apartat sencer
    clear()
    apartado = input("Qué apartado quieres eliminar? ")
    
    #Eliminem l'apartat sencer
    del pokepedia[apartado]
    clear()
    print("Apartado eliminado con éxito.")
    getch()

def eliminarPalabra():
    #Funcio per l'eliminació d'una paraula
    clear()
    apartado = input("De qué apartado es la palabra que quieres eliminar? ")
    palabra = input("Qué palabra quieres eliminar? ")
    
    #Si la clau existeix a la Pokepedia:
    if apartado in pokepedia.keys():
        #Eliminem la paraula donada
        del pokepedia[apartado][palabra]
        clear()
        print("Palabra eliminada con éxito.")
        getch()
    #Si no s'ha trobat dins de la Pokepedia, li comuniquem a l'usuari.    
    else:
        print("El apartado introducido no existe.")
        getch()
    
def entradaMenusSecundaris(eleccioMenuPrincipal):
    #Funció per seleccionar el menu secundari al que s'accedirà, per posteriorment gestionar l'acció desitjada a cada situació.
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
            elif eleccioSecundaria == MODIFICAR_DEFINICION:
                modificarDefinicion()
        
        #Añadir contenido
        case x if eleccioMenuPrincipal == AÑADIR_CONTENIDO:
            eleccioSecundaria = menuAñadirInfo()
            if eleccioSecundaria == AÑADIR_APARTADO:
                añadirApartado()
            elif eleccioSecundaria == AÑADIR_PALABRA:
                añadirPalabra()
        
        #Eliminar contenido
        case x if eleccioMenuPrincipal == ELIMINAR_CONTENIDO:
            eleccioSecundaria = menuEliminarInfo()
            if eleccioSecundaria == ELIMINAR_APARTADO:
                eliminarApartado()
            elif eleccioSecundaria == ELIMINAR_PALABRA:
                eliminarPalabra()
        
        #Opció no vàlida
        case _: print('Opció no vàlida')

#Main
while eleccioMenuPrincipal != 0:
    clear()
    eleccioMenuPrincipal = -1
    eleccioSecundaria = -1

    #Menu Principal
    eleccioMenuPrincipal = menuPrincipal()
    clear()
    entradaMenusSecundaris(eleccioMenuPrincipal)
    