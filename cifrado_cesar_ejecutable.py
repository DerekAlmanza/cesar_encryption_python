import cifrado_cesar as cesar
import os

def menu_interfaz():

    os.system('clear')
    print ("""Programa diseñado para efecturar el cifrado Cesar de un texto.
                Selecciona una opción:\n""")
    print ("\t1 - Cifrar caracteres puramente mayúsculas.")
    print ("\t2 - Cifrar caracteres puramente minúsculas.")
    print ("\t3 - Cifrar caracteres ya sean mayúsculas o minúsculas.")
    print ("\tSalir \n")


def menu():
    while True:
        menu_interfaz()
        opcion = input("Inserte opcion: ")
        print('')
        if opcion == "1":
            cesar.cifrado_mayus()
            break
        elif opcion == "2":
            cesar.cifrado_minus()
            break
        elif opcion == "3":
            cesar.cifrado_mayus_minus()
            break
        elif opcion == "salir":
            break
        else:
            print("No has pulsado una tecla correcta.")

menu()