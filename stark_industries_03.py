#Escobar Tobias Fabricio 
#1-J
#Clase 3

#Ejercicio Integrador Data Stark #02 (segunda entregada)

from os import system
system("cls")

from funciones_03 import *
# 6.Crear la función stark_marvel_app la cual recibirá por parámetro la lista de héroes
# y se encargará de la ejecución principal de nuestro programa.
# Utilizar if/elif o match según prefiera. Debe informar por consola en caso de
# seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las
# funciones con prefijo stark_ donde crea correspondiente.

menu = [" ",
        "1.Normalizar datos", "2.Mostrar heroes del género NB: ", "3.Mostrar heroe mas alto del genero F: ",
        "4.Mostrar heroe mas alto del genero M: ", "5.Mostrar heroe mas debil del genero M: ", 
        "6.Mostrar heroe mas debil del genero NB: ", "7.Mostrar fuerza promedio del genero NB: ",
        "8.Mostrar la cantidad de cada tipo de color de ojos: ", "9.Mostrar la cantidad de cada tipo de color de pelo: ",
        "10.Mostrar los heroes agrupados por color de ojos: ", "11.Mostrar los heroes agrupados por inteligencia: ",
        "12.Salir\n"]

def stark_marvel_app(lista:list):
    datos_normalizados = False
    seguir = True
    while seguir:
        respuesta = stark_menu_principal(lista)
        if datos_normalizados != True and respuesta > 1:
            print("Error. Usted debe inicializar los datos con la opcion n°1 antes de poder acceder a las demás.")
            break
        else:
            match respuesta:
                case 1:
                    stark_normalizar_datos(lista_personajes)
                    datos_normalizados = True
                case 2:
                    mostrar_nombres_nb(lista_personajes)
                case 3:
                    heroe_mas_alto(lista_personajes, "F")
                case 4:
                    heroe_mas_alto(lista_personajes, "M")
                case 5:
                    heroe_mas_debil(lista_personajes, "M")
                case 6:
                    heroe_mas_debil(lista_personajes, "NB")
                case 7:
                    fuerza_promedio(lista_personajes, "NB", "fuerza")
                case 8:
                    mostrar = mostrar_cantidad_tipos(lista_personajes, "color_ojos")
                    print(mostrar)
                case 9:
                    mostrar = mostrar_cantidad_tipos(lista_personajes, "color_pelo")
                    print(mostrar)
                case 10:
                    mostrar = mostrar_heroes_agrupados(lista_personajes, "color_ojos")
                    print(mostrar)
                case 11:
                    mostrar = mostrar_heroes_agrupados(lista_personajes, "color_pelo")
                    print(mostrar)
                case 12:
                    seguir = False
                    print("Salio del programa")

stark_marvel_app(menu)